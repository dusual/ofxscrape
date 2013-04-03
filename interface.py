#!/usr/bin/python
import abc


class StatementParserInterface(object):
    __metaclass__ = abc.ABCMeta
    """ The minimum objects that any statement parser has to implement"""
    def __init__(self):
        pass

    @abc.abstractmethod
    def bank_name(self):
        """ Return the Bank/ Financial Institution involved. This is also the function from which the parser recognizes what class to 
        for which statement"""
        return "Should not reach here "


    @abc.abstractmethod
    def branch_name(self):
        """ Details about the branch """
        return "Should not reach here "

    @abc.abstractmethod
    def account_details(self):
        """ Details about the account """
        return "Should not reach here "

    @abc.abstractmethod
    def transactions(self):
        return "Should not reach here "

    @abc.abstractmethod
    def balance(self):
        """ Current Balance in an account . Does this work for all kind of statements ??? """
        return "Should not reach here "

    def currency(self):
        """ Defaults to Rupees """
        return "INR"

    @abc.abstractmethod
    def time_period(self):
        """ Time period of the current statement """
        return "Should not reach here "


    def subclasses(self):   
		""" Get All subclasses / Plugins """
		return StatementParserInterface.__subclasses__()


                