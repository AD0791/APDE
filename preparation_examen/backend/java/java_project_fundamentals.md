# Java Project Structure & Build Tools: Complete Guide

## For Alexandro Disla — From Python/FastAPI to Java

---

# Part 1: Why Build Tools Exist

## The Problem They Solve

In Python, you have:
- `pip` for dependency management
- `requirements.txt` or `pyproject.toml` for listing dependencies
- Simple `python script.py` to run code

In Java, things are more complex because:

### 1. **Compilation Required**
Java must be compiled before running:
```bash
# Python - just run it
python app.py

# Java - compile first, then run
javac App.java        # Creates App.class
java App              # Runs the bytecode
```

### 2. **Classpath Management**
When you have dependencies, Java needs to know WHERE to find them:
```bash
# With 3 dependencies, this gets ugly fast:
javac -cp lib/gson.jar:lib/commons.jar:lib/logging.jar src/*.java
java -cp lib/gson.jar:lib/commons.jar:lib/logging.jar:. Main
```

### 3. **Transitive Dependencies**
If library A needs library B, which needs library C... you need ALL of them.

### 4. **Build Lifecycle**
Real projects need:
- Compile source code
- Compile test code
- Run tests
- Package into JAR/WAR
- Generate documentation
- Deploy artifacts

**Build tools automate ALL of this!**

---

# Part 2: Maven vs Gradle

## Maven (2004)

**Philosophy:** Convention over Configuration

```
Maven says: "Put your code HERE, your tests HERE, 
and I'll know exactly what to do."
```

### Maven Project Structure (STANDARD)
```
my-project/
├── pom.xml                    # Project Object Model (the config file)
├── src/
│   ├── main/
│   │   ├── java/              # Your source code
│   │   │   └── com/
│   │   │       └── example/
│   │   │           └── App.java
│   │   └── resources/         # Config files, properties, etc.
│   │       └── application.properties
│   └── test/
│       ├── java/              # Test code
│       │   └── com/
│       │       └── example/
│       │           └── AppTest.java
│       └── resources/         # Test resources
└── target/                    # Build output (generated, don't commit)
    ├── classes/               # Compiled .class files
    └── my-project-1.0.jar     # Final packaged JAR
```

### pom.xml Explained
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Project coordinates (unique identifier) -->
    <groupId>com.alexandro</groupId>      <!-- Like organization/namespace -->
    <artifactId>todo-cli</artifactId>      <!-- Project name -->
    <version>1.0.0</version>               <!-- Version -->
    <packaging>jar</packaging>             <!-- Output type: jar, war, pom -->
    
    <!-- Project metadata -->
    <name>Todo CLI Application</name>
    <description>A command-line todo list manager</description>
    
    <!-- Java version -->
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <!-- Dependencies (like requirements.txt) -->
    <dependencies>
        <!-- JSON processing -->
        <dependency>
            <groupId>com.google.code.gson</groupId>
            <artifactId>gson</artifactId>
            <version>2.10.1</version>
        </dependency>
        
        <!-- Testing (only needed for tests) -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.0</version>
            <scope>test</scope>  <!-- Not included in final JAR -->
        </dependency>
    </dependencies>
    
    <!-- Build configuration -->
    <build>
        <plugins>
            <!-- Create executable JAR with dependencies -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.5.0</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.alexandro.todo.Main</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Maven Commands
```bash
mvn compile          # Compile source code
mvn test             # Run tests
mvn package          # Create JAR file
mvn clean            # Delete target/ directory
mvn clean package    # Clean and rebuild
mvn install          # Install to local repository (~/.m2/)
mvn dependency:tree  # Show dependency tree

# Run with exec plugin
mvn exec:java -Dexec.mainClass="com.alexandro.todo.Main"
```

### Maven Lifecycle Phases
```
validate → compile → test → package → verify → install → deploy
                ↓
        Each phase runs all previous phases!
        
mvn package = validate + compile + test + package
```

---

## Gradle (2012)

**Philosophy:** Flexibility + Performance

```
Gradle says: "Here's a powerful scripting language. 
Build whatever you want, however you want."
```

### Gradle Project Structure
```
my-project/
├── build.gradle(.kts)         # Build script (Groovy or Kotlin DSL)
├── settings.gradle(.kts)      # Project settings
├── gradle/
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew                    # Unix wrapper script
├── gradlew.bat                # Windows wrapper script
├── src/
│   ├── main/
│   │   ├── java/
│   │   └── resources/
│   └── test/
│       ├── java/
│       └── resources/
└── build/                     # Output directory (like target/)
```

### build.gradle.kts (Kotlin DSL - Modern)
```kotlin
plugins {
    java
    application  // For CLI apps
}

group = "com.alexandro"
version = "1.0.0"

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

repositories {
    mavenCentral()  // Where to download dependencies
}

dependencies {
    // Main dependencies
    implementation("com.google.code.gson:gson:2.10.1")
    
    // Test dependencies
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}

application {
    mainClass.set("com.alexandro.todo.Main")
}

tasks.test {
    useJUnitPlatform()
}

// Create fat JAR with all dependencies
tasks.jar {
    manifest {
        attributes["Main-Class"] = "com.alexandro.todo.Main"
    }
    // Include all dependencies in JAR
    from(configurations.runtimeClasspath.get().map { if (it.isDirectory) it else zipTree(it) })
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}
```

### build.gradle (Groovy DSL - Classic)
```groovy
plugins {
    id 'java'
    id 'application'
}

group = 'com.alexandro'
version = '1.0.0'

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

repositories {
    mavenCentral()
}

dependencies {
    implementation 'com.google.code.gson:gson:2.10.1'
    testImplementation 'org.junit.jupiter:junit-jupiter:5.10.0'
}

application {
    mainClass = 'com.alexandro.todo.Main'
}

test {
    useJUnitPlatform()
}
```

### Gradle Commands
```bash
./gradlew build          # Compile, test, and package
./gradlew clean          # Delete build/ directory
./gradlew test           # Run tests
./gradlew run            # Run the application (with application plugin)
./gradlew tasks          # List all available tasks
./gradlew dependencies   # Show dependency tree

# The wrapper (gradlew) downloads correct Gradle version automatically!
```

---

## Maven vs Gradle: When to Use Which?

| Aspect | Maven | Gradle |
|--------|-------|--------|
| **Config Language** | XML (verbose) | Groovy/Kotlin (concise) |
| **Learning Curve** | Easier to start | Steeper but more powerful |
| **Build Speed** | Slower | Faster (incremental builds, caching) |
| **Flexibility** | Convention-based | Highly customizable |
| **IDE Support** | Excellent | Excellent |
| **Ecosystem** | Huge (older) | Growing fast |
| **Android** | No | Official tool |
| **Enterprise** | Very common | Increasingly popular |

### My Recommendation for You:
- **Start with Gradle (Kotlin DSL)** - It's more modern, faster, and the Kotlin DSL gives you IDE autocomplete
- **Know Maven basics** - Many existing projects use it, and the concepts transfer

---

# Part 3: Understanding the Package Structure

## Why Packages?

Packages are like Python modules/folders. They:
1. **Organize code** logically
2. **Prevent naming conflicts** (two `User` classes can exist in different packages)
3. **Control access** (package-private visibility)

### Package Naming Convention
```
Reverse domain name + project + module

com.alexandro.todo           # Base package
com.alexandro.todo.model     # Data classes
com.alexandro.todo.service   # Business logic
com.alexandro.todo.cli       # CLI handling
com.alexandro.todo.storage   # Persistence
```

### Package Declaration
Every Java file starts with its package:
```java
package com.alexandro.todo.model;

public class Task {
    // ...
}
```

### Directory Structure Matches Package
```
src/main/java/
└── com/
    └── alexandro/
        └── todo/
            ├── Main.java                    # package com.alexandro.todo
            ├── model/
            │   └── Task.java                # package com.alexandro.todo.model
            ├── service/
            │   └── TaskService.java         # package com.alexandro.todo.service
            ├── storage/
            │   └── JsonStorage.java         # package com.alexandro.todo.storage
            └── cli/
                └── CommandHandler.java      # package com.alexandro.todo.cli
```

---

# Part 4: Let's Build the Todo CLI!

## Project Setup with Gradle

### Step 1: Create Project Structure
```bash
mkdir todo-cli
cd todo-cli

# Create directory structure
mkdir -p src/main/java/com/alexandro/todo/{model,service,storage,cli}
mkdir -p src/main/resources
mkdir -p src/test/java/com/alexandro/todo
mkdir -p src/test/resources
```

### Step 2: Create Gradle Wrapper
```bash
# If you have Gradle installed:
gradle wrapper

# Or download wrapper files manually (we'll provide them)
```

### Step 3: settings.gradle.kts
```kotlin
rootProject.name = "todo-cli"
```

### Step 4: build.gradle.kts
```kotlin
plugins {
    java
    application
}

group = "com.alexandro"
version = "1.0.0"

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

repositories {
    mavenCentral()
}

dependencies {
    // JSON serialization
    implementation("com.google.code.gson:gson:2.10.1")
    
    // Better CLI argument parsing
    implementation("info.picocli:picocli:4.7.5")
    
    // Testing
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

application {
    mainClass.set("com.alexandro.todo.Main")
}

tasks.test {
    useJUnitPlatform()
}

// Create executable fat JAR
tasks.jar {
    manifest {
        attributes["Main-Class"] = "com.alexandro.todo.Main"
    }
    from(configurations.runtimeClasspath.get().map { 
        if (it.isDirectory) it else zipTree(it) 
    })
    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
    archiveBaseName.set("todo")
}
```

---

## The Complete Todo CLI Application

Now let's write all the Java code:

### Main.java - Entry Point
```java
package com.alexandro.todo;

import com.alexandro.todo.cli.TodoCommand;
import picocli.CommandLine;

/**
 * Application entry point.
 * Uses Picocli for professional CLI argument parsing.
 */
public class Main {
    
    public static void main(String[] args) {
        int exitCode = new CommandLine(new TodoCommand()).execute(args);
        System.exit(exitCode);
    }
}
```

### model/Task.java - The Data Model
```java
package com.alexandro.todo.model;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Objects;
import java.util.UUID;

/**
 * Represents a single task in the todo list.
 * Immutable where possible, with builder pattern for creation.
 */
public class Task {
    
    private final String id;
    private String title;
    private String description;
    private Priority priority;
    private boolean completed;
    private final LocalDateTime createdAt;
    private LocalDateTime completedAt;
    
    // Enum for type-safe priorities
    public enum Priority {
        LOW("○"),
        MEDIUM("◐"),
        HIGH("●"),
        URGENT("‼");
        
        private final String symbol;
        
        Priority(String symbol) {
            this.symbol = symbol;
        }
        
        public String getSymbol() {
            return symbol;
        }
    }
    
    // Private constructor - use Builder
    private Task(Builder builder) {
        this.id = builder.id != null ? builder.id : generateId();
        this.title = builder.title;
        this.description = builder.description;
        this.priority = builder.priority != null ? builder.priority : Priority.MEDIUM;
        this.completed = builder.completed;
        this.createdAt = builder.createdAt != null ? builder.createdAt : LocalDateTime.now();
        this.completedAt = builder.completedAt;
    }
    
    private static String generateId() {
        return UUID.randomUUID().toString().substring(0, 8);
    }
    
    // Builder Pattern
    public static class Builder {
        private String id;
        private String title;
        private String description;
        private Priority priority;
        private boolean completed;
        private LocalDateTime createdAt;
        private LocalDateTime completedAt;
        
        public Builder(String title) {
            this.title = Objects.requireNonNull(title, "Title cannot be null");
        }
        
        // For deserialization
        public Builder() {}
        
        public Builder id(String id) {
            this.id = id;
            return this;
        }
        
        public Builder title(String title) {
            this.title = title;
            return this;
        }
        
        public Builder description(String description) {
            this.description = description;
            return this;
        }
        
        public Builder priority(Priority priority) {
            this.priority = priority;
            return this;
        }
        
        public Builder completed(boolean completed) {
            this.completed = completed;
            return this;
        }
        
        public Builder createdAt(LocalDateTime createdAt) {
            this.createdAt = createdAt;
            return this;
        }
        
        public Builder completedAt(LocalDateTime completedAt) {
            this.completedAt = completedAt;
            return this;
        }
        
        public Task build() {
            if (title == null || title.isBlank()) {
                throw new IllegalStateException("Title is required");
            }
            return new Task(this);
        }
    }
    
    // Getters
    public String getId() { return id; }
    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public Priority getPriority() { return priority; }
    public boolean isCompleted() { return completed; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public LocalDateTime getCompletedAt() { return completedAt; }
    
    // Methods to modify task (return new instance for immutability pattern)
    public void markCompleted() {
        this.completed = true;
        this.completedAt = LocalDateTime.now();
    }
    
    public void markIncomplete() {
        this.completed = false;
        this.completedAt = null;
    }
    
    public void updateTitle(String newTitle) {
        this.title = Objects.requireNonNull(newTitle);
    }
    
    public void updateDescription(String newDescription) {
        this.description = newDescription;
    }
    
    public void updatePriority(Priority newPriority) {
        this.priority = newPriority;
    }
    
    // Display formatting
    public String toDisplayString() {
        String status = completed ? "✓" : " ";
        String prioritySymbol = priority.getSymbol();
        String dateStr = createdAt.format(DateTimeFormatter.ofPattern("MM/dd"));
        
        StringBuilder sb = new StringBuilder();
        sb.append(String.format("[%s] %s %s %s", status, prioritySymbol, id, title));
        
        if (description != null && !description.isBlank()) {
            sb.append(String.format("%n    └─ %s", description));
        }
        
        return sb.toString();
    }
    
    @Override
    public String toString() {
        return "Task{" +
                "id='" + id + '\'' +
                ", title='" + title + '\'' +
                ", completed=" + completed +
                ", priority=" + priority +
                '}';
    }
    
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Task task = (Task) o;
        return Objects.equals(id, task.id);
    }
    
    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
```

### model/TaskList.java - Collection of Tasks
```java
package com.alexandro.todo.model;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Represents the entire todo list.
 * Provides methods to query and filter tasks.
 */
public class TaskList {
    
    private final List<Task> tasks;
    
    public TaskList() {
        this.tasks = new ArrayList<>();
    }
    
    public TaskList(List<Task> tasks) {
        this.tasks = new ArrayList<>(tasks);
    }
    
    public void add(Task task) {
        tasks.add(task);
    }
    
    public boolean remove(String id) {
        return tasks.removeIf(t -> t.getId().equals(id));
    }
    
    public Optional<Task> findById(String id) {
        return tasks.stream()
                .filter(t -> t.getId().equals(id) || t.getId().startsWith(id))
                .findFirst();
    }
    
    public List<Task> findByTitle(String keyword) {
        String lowerKeyword = keyword.toLowerCase();
        return tasks.stream()
                .filter(t -> t.getTitle().toLowerCase().contains(lowerKeyword))
                .collect(Collectors.toList());
    }
    
    public List<Task> getAll() {
        return Collections.unmodifiableList(tasks);
    }
    
    public List<Task> getPending() {
        return tasks.stream()
                .filter(t -> !t.isCompleted())
                .collect(Collectors.toList());
    }
    
    public List<Task> getCompleted() {
        return tasks.stream()
                .filter(Task::isCompleted)
                .collect(Collectors.toList());
    }
    
    public List<Task> getByPriority(Task.Priority priority) {
        return tasks.stream()
                .filter(t -> t.getPriority() == priority)
                .collect(Collectors.toList());
    }
    
    public List<Task> getSortedByPriority() {
        return tasks.stream()
                .sorted(Comparator
                        .comparing(Task::isCompleted)  // Incomplete first
                        .thenComparing(Comparator.comparing(Task::getPriority).reversed())
                        .thenComparing(Task::getCreatedAt))
                .collect(Collectors.toList());
    }
    
    public int size() {
        return tasks.size();
    }
    
    public int pendingCount() {
        return (int) tasks.stream().filter(t -> !t.isCompleted()).count();
    }
    
    public int completedCount() {
        return (int) tasks.stream().filter(Task::isCompleted).count();
    }
    
    public boolean isEmpty() {
        return tasks.isEmpty();
    }
    
    public void clear() {
        tasks.clear();
    }
    
    public void clearCompleted() {
        tasks.removeIf(Task::isCompleted);
    }
}
```

### storage/TaskStorage.java - Interface for Persistence
```java
package com.alexandro.todo.storage;

import com.alexandro.todo.model.TaskList;

import java.io.IOException;

/**
 * Interface for task persistence.
 * Allows different storage implementations (JSON, SQLite, etc.)
 */
public interface TaskStorage {
    
    /**
     * Load tasks from storage.
     * @return TaskList containing all stored tasks
     * @throws IOException if reading fails
     */
    TaskList load() throws IOException;
    
    /**
     * Save tasks to storage.
     * @param taskList the tasks to save
     * @throws IOException if writing fails
     */
    void save(TaskList taskList) throws IOException;
    
    /**
     * Check if storage exists.
     * @return true if storage file/database exists
     */
    boolean exists();
}
```

### storage/JsonTaskStorage.java - JSON File Storage
```java
package com.alexandro.todo.storage;

import com.alexandro.todo.model.Task;
import com.alexandro.todo.model.TaskList;
import com.google.gson.*;

import java.io.*;
import java.lang.reflect.Type;
import java.nio.file.*;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

/**
 * JSON file-based storage implementation.
 * Stores tasks in ~/.todo/tasks.json
 */
public class JsonTaskStorage implements TaskStorage {
    
    private static final String DEFAULT_DIRECTORY = ".todo";
    private static final String DEFAULT_FILENAME = "tasks.json";
    
    private final Path storagePath;
    private final Gson gson;
    
    public JsonTaskStorage() {
        this(getDefaultPath());
    }
    
    public JsonTaskStorage(Path storagePath) {
        this.storagePath = storagePath;
        this.gson = createGson();
    }
    
    private static Path getDefaultPath() {
        String home = System.getProperty("user.home");
        return Paths.get(home, DEFAULT_DIRECTORY, DEFAULT_FILENAME);
    }
    
    private Gson createGson() {
        return new GsonBuilder()
                .setPrettyPrinting()
                .registerTypeAdapter(LocalDateTime.class, new LocalDateTimeAdapter())
                .create();
    }
    
    @Override
    public TaskList load() throws IOException {
        if (!exists()) {
            return new TaskList();
        }
        
        try (Reader reader = Files.newBufferedReader(storagePath)) {
            TaskData data = gson.fromJson(reader, TaskData.class);
            if (data == null || data.tasks == null) {
                return new TaskList();
            }
            return new TaskList(data.tasks);
        }
    }
    
    @Override
    public void save(TaskList taskList) throws IOException {
        // Ensure directory exists
        Path parent = storagePath.getParent();
        if (parent != null && !Files.exists(parent)) {
            Files.createDirectories(parent);
        }
        
        TaskData data = new TaskData();
        data.version = "1.0";
        data.tasks = new ArrayList<>(taskList.getAll());
        
        try (Writer writer = Files.newBufferedWriter(storagePath)) {
            gson.toJson(data, writer);
        }
    }
    
    @Override
    public boolean exists() {
        return Files.exists(storagePath);
    }
    
    public Path getStoragePath() {
        return storagePath;
    }
    
    // Wrapper class for JSON structure
    private static class TaskData {
        String version;
        List<Task> tasks;
    }
    
    // Custom adapter for LocalDateTime
    private static class LocalDateTimeAdapter 
            implements JsonSerializer<LocalDateTime>, JsonDeserializer<LocalDateTime> {
        
        private static final DateTimeFormatter FORMATTER = DateTimeFormatter.ISO_LOCAL_DATE_TIME;
        
        @Override
        public JsonElement serialize(LocalDateTime src, Type type, JsonSerializationContext context) {
            return new JsonPrimitive(src.format(FORMATTER));
        }
        
        @Override
        public LocalDateTime deserialize(JsonElement json, Type type, JsonDeserializationContext context) 
                throws JsonParseException {
            return LocalDateTime.parse(json.getAsString(), FORMATTER);
        }
    }
}
```

### service/TaskService.java - Business Logic
```java
package com.alexandro.todo.service;

import com.alexandro.todo.model.Task;
import com.alexandro.todo.model.TaskList;
import com.alexandro.todo.storage.TaskStorage;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

/**
 * Service layer containing business logic.
 * Coordinates between CLI and storage.
 */
public class TaskService {
    
    private final TaskStorage storage;
    private TaskList taskList;
    
    public TaskService(TaskStorage storage) {
        this.storage = storage;
    }
    
    /**
     * Initialize service by loading existing tasks.
     */
    public void initialize() throws IOException {
        this.taskList = storage.load();
    }
    
    /**
     * Add a new task.
     */
    public Task addTask(String title, String description, Task.Priority priority) throws IOException {
        Task task = new Task.Builder(title)
                .description(description)
                .priority(priority)
                .build();
        
        taskList.add(task);
        save();
        return task;
    }
    
    /**
     * Mark a task as completed.
     */
    public Optional<Task> completeTask(String id) throws IOException {
        Optional<Task> task = taskList.findById(id);
        task.ifPresent(t -> {
            t.markCompleted();
            try {
                save();
            } catch (IOException e) {
                throw new RuntimeException("Failed to save", e);
            }
        });
        return task;
    }
    
    /**
     * Mark a task as incomplete.
     */
    public Optional<Task> uncompleteTask(String id) throws IOException {
        Optional<Task> task = taskList.findById(id);
        task.ifPresent(t -> {
            t.markIncomplete();
            try {
                save();
            } catch (IOException e) {
                throw new RuntimeException("Failed to save", e);
            }
        });
        return task;
    }
    
    /**
     * Delete a task.
     */
    public boolean deleteTask(String id) throws IOException {
        boolean removed = taskList.remove(id);
        if (removed) {
            save();
        }
        return removed;
    }
    
    /**
     * Update task details.
     */
    public Optional<Task> updateTask(String id, String newTitle, String newDescription, 
                                      Task.Priority newPriority) throws IOException {
        Optional<Task> task = taskList.findById(id);
        task.ifPresent(t -> {
            if (newTitle != null && !newTitle.isBlank()) {
                t.updateTitle(newTitle);
            }
            if (newDescription != null) {
                t.updateDescription(newDescription);
            }
            if (newPriority != null) {
                t.updatePriority(newPriority);
            }
            try {
                save();
            } catch (IOException e) {
                throw new RuntimeException("Failed to save", e);
            }
        });
        return task;
    }
    
    /**
     * Get all tasks sorted by priority.
     */
    public List<Task> getAllTasks() {
        return taskList.getSortedByPriority();
    }
    
    /**
     * Get only pending tasks.
     */
    public List<Task> getPendingTasks() {
        return taskList.getPending();
    }
    
    /**
     * Get only completed tasks.
     */
    public List<Task> getCompletedTasks() {
        return taskList.getCompleted();
    }
    
    /**
     * Find a task by ID.
     */
    public Optional<Task> findTask(String id) {
        return taskList.findById(id);
    }
    
    /**
     * Search tasks by title.
     */
    public List<Task> searchTasks(String keyword) {
        return taskList.findByTitle(keyword);
    }
    
    /**
     * Clear all completed tasks.
     */
    public int clearCompleted() throws IOException {
        int count = taskList.completedCount();
        taskList.clearCompleted();
        save();
        return count;
    }
    
    /**
     * Get statistics.
     */
    public TaskStats getStats() {
        return new TaskStats(
                taskList.size(),
                taskList.pendingCount(),
                taskList.completedCount()
        );
    }
    
    private void save() throws IOException {
        storage.save(taskList);
    }
    
    // Stats record (Java 16+) or class
    public record TaskStats(int total, int pending, int completed) {
        public double completionRate() {
            return total == 0 ? 0 : (double) completed / total * 100;
        }
    }
}
```

### cli/TodoCommand.java - Main CLI Command
```java
package com.alexandro.todo.cli;

import com.alexandro.todo.model.Task;
import com.alexandro.todo.service.TaskService;
import com.alexandro.todo.storage.JsonTaskStorage;
import picocli.CommandLine;
import picocli.CommandLine.*;

import java.io.IOException;
import java.util.List;
import java.util.concurrent.Callable;

/**
 * Main CLI command with subcommands.
 * Uses Picocli for professional argument parsing.
 */
@Command(
    name = "todo",
    description = "A simple command-line todo list manager",
    version = "1.0.0",
    mixinStandardHelpOptions = true,  // Adds --help and --version
    subcommands = {
        TodoCommand.Add.class,
        TodoCommand.ListTasks.class,
        TodoCommand.Complete.class,
        TodoCommand.Delete.class,
        TodoCommand.Update.class,
        TodoCommand.Search.class,
        TodoCommand.Clear.class,
        TodoCommand.Stats.class
    }
)
public class TodoCommand implements Callable<Integer> {
    
    @Override
    public Integer call() {
        // Default action: show pending tasks
        CommandLine.usage(this, System.out);
        return 0;
    }
    
    // ============ ADD COMMAND ============
    @Command(name = "add", description = "Add a new task")
    static class Add implements Callable<Integer> {
        
        @Parameters(index = "0", description = "Task title")
        private String title;
        
        @Option(names = {"-d", "--description"}, description = "Task description")
        private String description;
        
        @Option(names = {"-p", "--priority"}, 
                description = "Priority: LOW, MEDIUM, HIGH, URGENT",
                defaultValue = "MEDIUM")
        private Task.Priority priority;
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                Task task = service.addTask(title, description, priority);
                System.out.println("✓ Added task: " + task.getId());
                System.out.println(task.toDisplayString());
                return 0;
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ LIST COMMAND ============
    @Command(name = "list", aliases = {"ls"}, description = "List tasks")
    static class ListTasks implements Callable<Integer> {
        
        @Option(names = {"-a", "--all"}, description = "Show all tasks including completed")
        private boolean showAll;
        
        @Option(names = {"-c", "--completed"}, description = "Show only completed tasks")
        private boolean showCompleted;
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                List<Task> tasks;
                String header;
                
                if (showCompleted) {
                    tasks = service.getCompletedTasks();
                    header = "Completed Tasks";
                } else if (showAll) {
                    tasks = service.getAllTasks();
                    header = "All Tasks";
                } else {
                    tasks = service.getPendingTasks();
                    header = "Pending Tasks";
                }
                
                if (tasks.isEmpty()) {
                    System.out.println("No tasks found.");
                    return 0;
                }
                
                System.out.println("\n" + header + " (" + tasks.size() + ")");
                System.out.println("─".repeat(40));
                
                for (Task task : tasks) {
                    System.out.println(task.toDisplayString());
                }
                
                System.out.println();
                return 0;
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ COMPLETE COMMAND ============
    @Command(name = "done", aliases = {"complete"}, description = "Mark task as completed")
    static class Complete implements Callable<Integer> {
        
        @Parameters(index = "0", description = "Task ID (or prefix)")
        private String id;
        
        @Option(names = {"-u", "--undo"}, description = "Mark as incomplete instead")
        private boolean undo;
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                var result = undo 
                        ? service.uncompleteTask(id) 
                        : service.completeTask(id);
                
                if (result.isPresent()) {
                    String action = undo ? "marked incomplete" : "completed";
                    System.out.println("✓ Task " + action + ": " + result.get().getTitle());
                    return 0;
                } else {
                    System.err.println("Task not found: " + id);
                    return 1;
                }
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ DELETE COMMAND ============
    @Command(name = "delete", aliases = {"rm", "remove"}, description = "Delete a task")
    static class Delete implements Callable<Integer> {
        
        @Parameters(index = "0", description = "Task ID (or prefix)")
        private String id;
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                if (service.deleteTask(id)) {
                    System.out.println("✓ Task deleted");
                    return 0;
                } else {
                    System.err.println("Task not found: " + id);
                    return 1;
                }
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ UPDATE COMMAND ============
    @Command(name = "update", aliases = {"edit"}, description = "Update a task")
    static class Update implements Callable<Integer> {
        
        @Parameters(index = "0", description = "Task ID (or prefix)")
        private String id;
        
        @Option(names = {"-t", "--title"}, description = "New title")
        private String title;
        
        @Option(names = {"-d", "--description"}, description = "New description")
        private String description;
        
        @Option(names = {"-p", "--priority"}, description = "New priority")
        private Task.Priority priority;
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                var result = service.updateTask(id, title, description, priority);
                
                if (result.isPresent()) {
                    System.out.println("✓ Task updated");
                    System.out.println(result.get().toDisplayString());
                    return 0;
                } else {
                    System.err.println("Task not found: " + id);
                    return 1;
                }
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ SEARCH COMMAND ============
    @Command(name = "search", aliases = {"find"}, description = "Search tasks by title")
    static class Search implements Callable<Integer> {
        
        @Parameters(index = "0", description = "Search keyword")
        private String keyword;
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                List<Task> results = service.searchTasks(keyword);
                
                if (results.isEmpty()) {
                    System.out.println("No tasks found matching: " + keyword);
                    return 0;
                }
                
                System.out.println("\nSearch Results (" + results.size() + ")");
                System.out.println("─".repeat(40));
                
                for (Task task : results) {
                    System.out.println(task.toDisplayString());
                }
                
                return 0;
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ CLEAR COMMAND ============
    @Command(name = "clear", description = "Clear completed tasks")
    static class Clear implements Callable<Integer> {
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                int cleared = service.clearCompleted();
                System.out.println("✓ Cleared " + cleared + " completed task(s)");
                return 0;
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ STATS COMMAND ============
    @Command(name = "stats", description = "Show statistics")
    static class Stats implements Callable<Integer> {
        
        @Override
        public Integer call() {
            try {
                TaskService service = createService();
                var stats = service.getStats();
                
                System.out.println("\n📊 Task Statistics");
                System.out.println("─".repeat(30));
                System.out.printf("Total tasks:     %d%n", stats.total());
                System.out.printf("Pending:         %d%n", stats.pending());
                System.out.printf("Completed:       %d%n", stats.completed());
                System.out.printf("Completion rate: %.1f%%%n", stats.completionRate());
                System.out.println();
                
                return 0;
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
                return 1;
            }
        }
    }
    
    // ============ HELPER ============
    private static TaskService createService() throws IOException {
        TaskService service = new TaskService(new JsonTaskStorage());
        service.initialize();
        return service;
    }
}
```

---

## Unit Tests

### TaskTest.java
```java
package com.alexandro.todo;

import com.alexandro.todo.model.Task;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;

import static org.junit.jupiter.api.Assertions.*;

class TaskTest {
    
    @Test
    @DisplayName("Should create task with required fields")
    void createTask() {
        Task task = new Task.Builder("Buy groceries").build();
        
        assertNotNull(task.getId());
        assertEquals("Buy groceries", task.getTitle());
        assertEquals(Task.Priority.MEDIUM, task.getPriority()); // Default
        assertFalse(task.isCompleted());
        assertNotNull(task.getCreatedAt());
    }
    
    @Test
    @DisplayName("Should create task with all fields")
    void createTaskWithAllFields() {
        Task task = new Task.Builder("Important meeting")
                .description("Discuss Q4 plans")
                .priority(Task.Priority.HIGH)
                .build();
        
        assertEquals("Important meeting", task.getTitle());
        assertEquals("Discuss Q4 plans", task.getDescription());
        assertEquals(Task.Priority.HIGH, task.getPriority());
    }
    
    @Test
    @DisplayName("Should throw exception for null title")
    void shouldRejectNullTitle() {
        assertThrows(NullPointerException.class, () -> {
            new Task.Builder(null).build();
        });
    }
    
    @Test
    @DisplayName("Should throw exception for blank title")
    void shouldRejectBlankTitle() {
        assertThrows(IllegalStateException.class, () -> {
            new Task.Builder("   ").build();
        });
    }
    
    @Test
    @DisplayName("Should mark task as completed")
    void completeTask() {
        Task task = new Task.Builder("Test task").build();
        assertFalse(task.isCompleted());
        
        task.markCompleted();
        
        assertTrue(task.isCompleted());
        assertNotNull(task.getCompletedAt());
    }
    
    @Test
    @DisplayName("Should mark completed task as incomplete")
    void uncompleteTask() {
        Task task = new Task.Builder("Test task").build();
        task.markCompleted();
        assertTrue(task.isCompleted());
        
        task.markIncomplete();
        
        assertFalse(task.isCompleted());
        assertNull(task.getCompletedAt());
    }
    
    @Test
    @DisplayName("Tasks with same ID should be equal")
    void taskEquality() {
        Task task1 = new Task.Builder("Task 1").id("abc123").build();
        Task task2 = new Task.Builder("Task 2").id("abc123").build();
        
        assertEquals(task1, task2);
        assertEquals(task1.hashCode(), task2.hashCode());
    }
}
```

### TaskServiceTest.java
```java
package com.alexandro.todo;

import com.alexandro.todo.model.Task;
import com.alexandro.todo.model.TaskList;
import com.alexandro.todo.service.TaskService;
import com.alexandro.todo.storage.TaskStorage;
import org.junit.jupiter.api.*;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class TaskServiceTest {
    
    private TaskService service;
    private InMemoryStorage storage;
    
    @BeforeEach
    void setUp() throws IOException {
        storage = new InMemoryStorage();
        service = new TaskService(storage);
        service.initialize();
    }
    
    @Test
    @DisplayName("Should add a new task")
    void addTask() throws IOException {
        Task task = service.addTask("Buy milk", "From the store", Task.Priority.LOW);
        
        assertNotNull(task);
        assertEquals("Buy milk", task.getTitle());
        assertEquals("From the store", task.getDescription());
        assertEquals(Task.Priority.LOW, task.getPriority());
        assertEquals(1, service.getAllTasks().size());
    }
    
    @Test
    @DisplayName("Should complete a task")
    void completeTask() throws IOException {
        Task task = service.addTask("Test", null, Task.Priority.MEDIUM);
        
        var result = service.completeTask(task.getId());
        
        assertTrue(result.isPresent());
        assertTrue(result.get().isCompleted());
    }
    
    @Test
    @DisplayName("Should delete a task")
    void deleteTask() throws IOException {
        Task task = service.addTask("Test", null, Task.Priority.MEDIUM);
        assertEquals(1, service.getAllTasks().size());
        
        boolean deleted = service.deleteTask(task.getId());
        
        assertTrue(deleted);
        assertEquals(0, service.getAllTasks().size());
    }
    
    @Test
    @DisplayName("Should search tasks by title")
    void searchTasks() throws IOException {
        service.addTask("Buy groceries", null, Task.Priority.MEDIUM);
        service.addTask("Buy clothes", null, Task.Priority.LOW);
        service.addTask("Call mom", null, Task.Priority.HIGH);
        
        List<Task> results = service.searchTasks("buy");
        
        assertEquals(2, results.size());
    }
    
    @Test
    @DisplayName("Should clear completed tasks")
    void clearCompleted() throws IOException {
        Task task1 = service.addTask("Task 1", null, Task.Priority.MEDIUM);
        Task task2 = service.addTask("Task 2", null, Task.Priority.MEDIUM);
        service.addTask("Task 3", null, Task.Priority.MEDIUM);
        
        service.completeTask(task1.getId());
        service.completeTask(task2.getId());
        
        int cleared = service.clearCompleted();
        
        assertEquals(2, cleared);
        assertEquals(1, service.getAllTasks().size());
    }
    
    // In-memory storage for testing
    private static class InMemoryStorage implements TaskStorage {
        private TaskList taskList = new TaskList();
        
        @Override
        public TaskList load() {
            return taskList;
        }
        
        @Override
        public void save(TaskList taskList) {
            this.taskList = taskList;
        }
        
        @Override
        public boolean exists() {
            return true;
        }
    }
}
```

---

# Part 5: Building and Running

## With Gradle

```bash
# Navigate to project
cd todo-cli

# Build the project (compiles, runs tests, creates JAR)
./gradlew build

# Run tests only
./gradlew test

# Run the application
./gradlew run --args="add 'Buy groceries' -p HIGH"

# Create JAR file
./gradlew jar

# Run the JAR
java -jar build/libs/todo-1.0.0.jar list
```

## Create Alias for Easy Use

```bash
# Add to ~/.bashrc or ~/.zshrc
alias todo="java -jar /path/to/todo-1.0.0.jar"

# Now use it like:
todo add "Learn Java build tools" -p HIGH
todo list
todo done abc123
todo stats
```

---

# Part 6: IDE Setup

## IntelliJ IDEA (Recommended)

1. **Open Project**: File → Open → Select the `todo-cli` folder
2. IntelliJ auto-detects Gradle and imports the project
3. **Run Configuration**: 
   - Click "Add Configuration" 
   - Add "Application"
   - Main class: `com.alexandro.todo.Main`
   - Program arguments: `add "Test task"`

## VS Code

1. Install extensions:
   - "Extension Pack for Java"
   - "Gradle for Java"
2. Open the folder
3. VS Code auto-detects Gradle project

---

# Summary: Key Concepts

| Concept | What It Means |
|---------|---------------|
| **Build Tool** | Automates compile, test, package, dependency management |
| **Maven** | XML-based, convention-over-configuration |
| **Gradle** | DSL-based (Groovy/Kotlin), flexible, faster |
| **pom.xml** | Maven configuration file |
| **build.gradle** | Gradle configuration file |
| **GAV** | GroupId:ArtifactId:Version - unique dependency identifier |
| **Package** | Java namespace (maps to directory structure) |
| **JAR** | Java ARchive - packaged application |
| **Fat JAR** | JAR with all dependencies included |

## Project Structure Checklist

```
my-project/
├── build.gradle.kts (or pom.xml)
├── settings.gradle.kts
├── src/
│   ├── main/
│   │   ├── java/          ← Your code
│   │   └── resources/     ← Config files
│   └── test/
│       ├── java/          ← Test code
│       └── resources/     ← Test config
├── gradle/wrapper/        ← Gradle wrapper
└── .gitignore
```

## What to Put in .gitignore

```gitignore
# Gradle
.gradle/
build/

# Maven
target/

# IDE
.idea/
*.iml
.vscode/

# OS
.DS_Store
Thumbs.db
```

You now have everything you need to build Java projects from scratch! 🎉
