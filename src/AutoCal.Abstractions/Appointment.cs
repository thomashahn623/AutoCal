namespace AutoCal.Abstractions;

public abstract class AppointmentBase
{
    public string Id { get; set; }                           // Systeminterne ID
    public string ExternalId { get; set; }                   // z. B. Google/Outlook/CalDAV-ID

    public string Title { get; set; }
    public string Description { get; set; }
    public string Location { get; set; }

    public DateTimeOffset StartTime { get; set; }
    public DateTimeOffset EndTime { get; set; }

    public bool IsAllDay { get; set; }                       // Wichtig für CalDAV & Google
    public bool IsRecurring { get; set; }                    // Marker für Serien
    public string RecurrenceRule { get; set; }               // iCal RRULE für Wiederholungen

    public BusyState BusyState { get; set; }                 // Frei/Belegt/Tentative/Etc.

    public List<Attendee> Attendees { get; set; } = new();   // Teilnehmer – universell nutzbar
    public Dictionary<string, string> Metadata { get; set; } = new(); // Für systemabhängige Felder

    public List<string> Categories { get; set; } = new();

}
