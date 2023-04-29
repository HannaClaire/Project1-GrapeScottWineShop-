from flask import Flask, render_template
from flask import Blueprint
from models.wine import Wine
import repositories.wine_repository as wine_repo
import repositories.producer_repository as producer_repo
