import { useEffect, useState } from "react";
import { createNote, fetchNotes } from "./services/api";
import "./styles.css";

function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  async function loadNotes() {
    setIsLoading(true);
    setError("");
    try {
      const data = await fetchNotes();
      setNotes(data);
    } catch (err) {
      setError(err.message || "Unable to load notes.");
    } finally {
      setIsLoading(false);
    }
  }

  useEffect(() => {
    loadNotes();
  }, []);

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    try {
      await createNote({ title, body });
      setTitle("");
      setBody("");
      await loadNotes();
    } catch (err) {
      setError(err.message || "Unable to create note.");
    }
  }

  return (
    <main className="page">
      <header className="header">
        <h1>Notes Application</h1>
        <p>Week 1 baseline: create and list notes with FastAPI + SQLAlchemy.</p>
      </header>

      <section className="panel">
        <h2>Create Note</h2>
        <form onSubmit={handleSubmit} className="note-form">
          <label>
            Title
            <input
              type="text"
              value={title}
              onChange={(event) => setTitle(event.target.value)}
              minLength={1}
              maxLength={200}
              required
            />
          </label>
          <label>
            Body
            <textarea
              value={body}
              onChange={(event) => setBody(event.target.value)}
              minLength={1}
              rows={4}
              required
            />
          </label>
          <button type="submit">Save Note</button>
        </form>
      </section>

      <section className="panel">
        <h2>Your Notes</h2>
        {isLoading && <p>Loading notes...</p>}
        {!isLoading && error && <p className="error">{error}</p>}
        {!isLoading && !error && notes.length === 0 && <p>No notes yet. Create your first note.</p>}
        {!isLoading && !error && notes.length > 0 && (
          <ul className="notes-list">
            {notes.map((note) => (
              <li key={note.id} className="note-item">
                <h3>{note.title}</h3>
                <p>{note.body}</p>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  );
}

export default App;
