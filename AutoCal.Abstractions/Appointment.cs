namespace AutoCal.Abstractions;

// Represents an appointment (can be extended as needed)
public class Appointment
{
    public string Id { get; set; }
    public string Title { get; set; }
    public DateTimeOffset StartTime { get; set; }
    public DateTimeOffset EndTime { get; set; }
    public string Location { get; set; }
    public string Description { get; set; }
    public BusyState BusyState { get; set; }
}
