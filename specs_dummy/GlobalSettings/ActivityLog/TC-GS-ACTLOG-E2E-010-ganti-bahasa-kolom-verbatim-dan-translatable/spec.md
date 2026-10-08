---
id: TC-GS-ACTLOG-E2E-010-ganti-bahasa-kolom-verbatim-dan-translatable
title: "Dukungan Multibahasa: Nilai Kolom Verbatim Tetap dan Nilai Translatable Mengikuti Pilihan Bahasa"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-27
coverage:
  web: automated
---

# Dukungan Multibahasa: Nilai Kolom Verbatim Tetap dan Nilai Translatable Mengikuti Pilihan Bahasa

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Terdapat data log Session (Login Failed) dan User Action (Edit)
- Konfigurasi Date Format General Settings: DD/MM/YY

## Test Steps

### Tinjauan Awal Bahasa Inggris (En)
1. Buka Tab Session dalam bahasa default (Inggris).
2. Catat nilai satu baris Login Failed pada kolom: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device / Browser.
3. Buka Tab User Action, catat satu baris Edit pada kolom: Date, Action, Object, Name, Field, Old Value, New Value, Modified By.
### Pergantian Bahasa ke Non-Inggris
4. Buka pemilih bahasa (Language Picker) di header aplikasi, pilih bahasa non-Inggris (misal Bahasa Indonesia).
5. Buka kembali Tab Session.
6. Verifikasi kolom Verbatim tidak berubah teksnya: Date, User, Employee ID, Position, Division, IP Address, Device / Browser.
7. Verifikasi kolom Translatable diterjemahkan ke bahasa aktif: Activity, Status, dan Note.
8. Buka Tab User Action.
9. Verifikasi kolom Verbatim tidak berubah: Date, Name, Old Value, New Value, Modified By.
10. Verifikasi kolom Translatable diterjemahkan ke bahasa aktif: Action, Object, dan Field.

## Notes

- Pemisahan strict antara nilai verbatim (identitas/snapshot) dan translatable (istilah sistem) menjaga integritas data audit.
