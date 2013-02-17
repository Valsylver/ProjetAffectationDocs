package fr.affectation.domain.choice;

import java.util.ArrayList;
import java.util.List;

import javax.persistence.Column;
import javax.persistence.ElementCollection;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table
public class NewChoice {
	
	public static final int NUMBER_CHOICES_IC = 5;
	
	public static final int NUMBER_CHOICES_JS = 5;
	
	@Id
	private String login;
	
	@ElementCollection
	@Column
	private List<String> icChoices = new ArrayList<String>();
	
	@ElementCollection
	@Column
	private List<String> jsChoices = new ArrayList<String>();
	
	public NewChoice(){
		for (int i=0; i<NUMBER_CHOICES_IC; i++){
			icChoices.add("");
		}
		for (int i=0; i<NUMBER_CHOICES_JS; i++){
			jsChoices.add("");
		}
	}
	
	public void setIcChoiceByOrder(int order, String abbreviation){
		if (!((order <= 0) || (order>NUMBER_CHOICES_IC))){
			icChoices.set(order-1, abbreviation);
		}
	}
	
	public void setJsChoiceByOrder(int order, String abbreviation){
		if (!((order <= 0) || (order>NUMBER_CHOICES_JS))){
			jsChoices.set(order-1, abbreviation);
		}
	}

	public String getLogin() {
		return login;
	}

	public void setLogin(String login) {
		this.login = login;
	}

	public List<String> getIcChoices() {
		return icChoices;
	}

	public void setIcChoices(ArrayList<String> icChoices) {
		this.icChoices = icChoices;
	}

	public List<String> getJsChoices() {
		return jsChoices;
	}

	public void setJsChoices(ArrayList<String> jsChoices) {
		this.jsChoices = jsChoices;
	}

}
