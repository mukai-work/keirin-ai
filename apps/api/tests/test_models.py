from src.models import ShapValue


def test_shap_value_indexes() -> None:
    index_names = {idx.name for idx in ShapValue.__table__.indexes}
    assert "ix_shap_race_id" in index_names
    assert "ix_shap_feature_name" in index_names
    assert "ix_shap_model_version" in index_names
