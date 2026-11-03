---
id: TC-AC-SU-E2E-196-tab-system-log-search-per-kolom
title: "Tab System Log: Search per Kolom Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-412
coverage:
  web: automated
---

# Tab System Log: Search per Kolom Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-196` (email `janesmith+{runId}-196@qwertysystem.net`) sebagai aktor dengan 2 entri System Log: (1) Action `Deactivate`, Object `Total Control`, Name `John Doe {runId}-196`, Field `Access Level`, Old Value `Active`, New Value `Inactive`; (2) Action `Edit`, Object `Global Role`, Name `Sarah Lee {runId}-196`, Field `Manage group — Update`, Old Value `Read`, New Value `Update`.

| Search per kolom | Keyword huruf kecil | Keyword huruf kapital | Nilai yang cocok |
|---|---|---|---|
| Action | `deact` | `DEACT` | `Deactivate` |
| Object | `total con` | `TOTAL CON` | `Total Control` |
| Name | `john` | `JOHN` | `John Doe {runId}-196` |
| Field | `acce` | `ACCE` | `Access Level` |
| Old Value | `acti` | `ACTI` | `Active` |
| New Value | `inac` | `INAC` | `Inactive` |

- Kemampuan teknis: kemampuan seed entri System Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-412: Search Tab System Log per kolom kelas teks

1. Cari `Jane Smith {runId}-196` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`
3. Klik icon Search
4. Ganti isi kotak Search dengan keyword huruf kecil pada baris tabel 'Search per kolom', tekan Enter
5. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
6. Ganti isi kotak Search dengan keyword huruf kapital pada baris tabel yang sama, tekan Enter
7. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
8. Klik icon `(←)` pada kotak Search

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah Search per kolom diulang per baris tabel 'Search per kolom': langkah 4 sampai 7 (6 kolom, tiap kolom dua keyword). Klik icon Search sebelum iterasi pertama dan klik `(←)` sesudah iterasi terakhir adalah langkah penghubung. Pembagian TC lintas spec: TC-411 dan TC-413 ada di spec 115.
- Temuan untuk QA:
  - Search diterapkan pada seluruh kolom searchable, sehingga keyword seperti `acti` juga dapat cocok dengan kolom lain (mis. `Activation Email` bila ada); TC tidak menyatakan apakah hasil hanya dari kolom yang disebut. Spec hanya mengasersi bahwa baris yang memuat nilai kolom itu tampil.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
