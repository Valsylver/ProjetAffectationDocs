package fr.affectation.service.newchoice;

import java.util.List;

import javax.inject.Inject;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.transaction.annotation.Transactional;

import fr.affectation.domain.choice.NewChoice;
import fr.affectation.domain.specialization.Specialization;

public class NewChoiceServiceImpl implements NewChoiceService {
	
	@Inject
	private SessionFactory sessionFactory;

	@Override
	@Transactional
	public void saveChoice(NewChoice choice) {
		Session session = sessionFactory.getCurrentSession();
		session.saveOrUpdate(choice);
	}

	@Override
	@Transactional(readOnly = true)
	public List<String> retrieveIcChoices(String login) {
		Session session = sessionFactory.getCurrentSession();
		NewChoice nc = (NewChoice) session.get(NewChoice.class, login);
		return nc != null ? nc.getIcChoices() : null;
	}
	
	@Override
	@Transactional(readOnly = true)
	public List<String> retrieveJsChoices(String login) {
		Session session = sessionFactory.getCurrentSession();
		NewChoice nc = (NewChoice) session.get(NewChoice.class, login);
		return nc != null ? nc.getJsChoices() : null;
	}

	@Override
	@SuppressWarnings("unchecked")
	@Transactional(readOnly = true)
	public List<String> findLoginsByOrderChoiceAndSpecialization(int order, Specialization specialization) {
		Session session = sessionFactory.getCurrentSession();
		String querySelect = "select choice.login from NewChoice choice where choice.";
		querySelect += specialization.getType().equals("JobSector") ? "ic" : "js";
		querySelect += "Choices";
		querySelect += "[" + order + "]";
		querySelect += "=:abbreviation";
		System.out.println(session == null);
		Query query = session.createQuery(querySelect);
		query.setString("abbreviation", specialization.getAbbreviation());
		return query.list();
	}

}
