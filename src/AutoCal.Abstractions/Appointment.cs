namespace AutoCal.Abstractions;

public class Appointment
{
    public string Id { get; set; }
    public string Title { get; set; }
    public string Description { get; set; }
    public DateTimeOffset StartTime { get; set; }
    public DateTimeOffset EndTime { get; set; }
    public BusyState BusyState { get; set; }
    public List<string> Categories { get; set; } = new();
}
