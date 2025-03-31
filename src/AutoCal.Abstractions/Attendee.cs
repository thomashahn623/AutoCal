namespace AutoCal.Abstractions;

public class Attendee
{
    public string Email { get; set; }
    public string Name { get; set; }
    public ParticipationStatus Status { get; set; } // Accepted, Declined, Tentative, etc.
}
