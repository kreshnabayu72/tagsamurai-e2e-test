---
id: TC-GS-POS-E2E-045-parity-create-missing-positions
title: Parity Hasil Create Missing Positions dengan Create Manual
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-241
  - TC-GS-POS-242
coverage:
  web: automated
---

# Parity Hasil Create Missing Positions dengan Create Manual

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tersedia fitur `Create Missing Positions` dari modul Import (IMP-LOGIC-11) untuk menghasilkan Position baru otomatis.
- Dataset Import mengandung nama Position yang belum ada di master Position.

## Test Steps

### A. Buat manual vs Create Missing Positions

1. Siapkan nama Position `X-Manual` dan `X-Auto` (terpisah).
2. Buat `X-Manual` secara manual via `[+ Position]` → Submit.
3. Jalankan alur Import yang memicu `[Create Missing Positions]` untuk menciptakan `X-Auto` (sesuai modul Import).
4. Buka `Global Settings > User > Position`, temukan kedua row.

### B. Parity tampilan tabel utama

5. Verifikasi kedua row tampil identik di tabel utama (kolom Name, Last Updated format konsisten, tidak ada indikator asal-usul import).
6. Verifikasi tidak ada badge/label khusus yang membedakan `X-Auto` hasil Create Missing Positions vs manual.

### C. Parity entri Changelog

7. Buka Popup Changelog Position.
8. Cari entri Create untuk `X-Auto` dan untuk `X-Manual`.
9. Verifikasi entri Create untuk `X-Auto` adalah Action `Create` polos (BUKAN `Create (Import)`).
10. Verifikasi struktur log (Action, Name, Field, Old Value `—`, New Value, Modified By) identik antar keduanya.
11. Verifikasi Modified By sesuai aktor yang memicu aksi (tidak otomatis "System" khusus untuk jalur ini) sesuai definisi TC-GS-POS-254.

## Notes

- Parity memastikan jalur otomatis tidak menciptakan perbedaan semantik di master data & audit log (kecuali konteks pemicu yang tercatat secara wajar).
