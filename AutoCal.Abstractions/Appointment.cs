namespace AutoCal.Abstractions;

// Represents an appointment (can be extended as needed)
public class Appointment
{
    public string Id { get; set; }
    public string Title { get; set; }
    public DateTime StartTime { get; set; }
    public DateTime EndTime { get; set; }
    public string Location { get; set; }
    public string Description { get; set; }
    public BusyState BusyState { get; set; }
}
