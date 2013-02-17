package fr.affectation.service.newchoice;

import java.util.List;

import fr.affectation.domain.choice.NewChoice;
import fr.affectation.domain.specialization.Specialization;

public interface NewChoiceService {
	
	public void saveChoice(NewChoice choice);
	
	public List<String> retrieveIcChoices(String login);
	
	public List<String> retrieveJsChoices(String login);
	
	public List<String> findLoginsByOrderChoiceAndSpecialization(int order, Specialization specialization);

}
