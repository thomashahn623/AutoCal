namespace AutoCal.Abstractions;

public interface IAppointment
{
    string Id { get; set; }
    string Title { get; set; }
    string Description { get; set; }
    DateTimeOffset StartTime { get; set; }
    DateTimeOffset EndTime { get; set; }
    BusyState BusyState { get; set; }
    List<string> Categories { get; set; }
}
