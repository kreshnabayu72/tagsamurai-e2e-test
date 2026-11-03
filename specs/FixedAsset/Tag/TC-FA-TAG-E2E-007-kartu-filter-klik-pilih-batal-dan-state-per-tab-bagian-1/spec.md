---
id: TC-FA-TAG-E2E-007-kartu-filter-klik-pilih-batal-dan-state-per-tab-bagian-1
title: "Kartu Filter: Klik untuk Memfilter, Klik Ulang untuk Membatalkan, Satu Kartu Aktif, dan Popup Detail Not Paired Yet"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-31
  - TC-FA-TAG-32
  - TC-FA-TAG-33
  - TC-FA-TAG-34
  - TC-FA-TAG-35
  - TC-FA-TAG-36
  - TC-FA-TAG-37
  - TC-FA-TAG-38
coverage:
  web: automated
---

# Kartu Filter: Klik untuk Memfilter, Klik Ulang untuk Membatalkan, Satu Kartu Aktif, dan Popup Detail Not Paired Yet

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- Data Pre-setup tab Paired (hanya dibaca, tidak diubah):

  | Asset Name | Group | TAG Type | Total Assets | Reported | Non-standard | Not Paired Yet |
  |---|---|---|---|---|---|---|
  | Excavator 20 Ton | Plant A | RFID | 20 | 0 | 0 | 2 |
  | Excavator 20 Ton | Plant B | RFID | 20 | 2 | 5 | 0 |
  | Laptop Pro 14 | HQ | NFC, QR | 25 | 1 | 0 | 2 |
  | Forklift Manual | Plant A | Non TAG | 10 | 0 | 3 | 0 |

- Data TC-FA-TAG-38: grup Excavator 20 Ton / Plant A memuat dua aset Not Paired Yet dengan TAG Code `—`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE, dilewati bila data sudah ada). Nama dan kode literal tidak diberi suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah (suite.md).
- Tidak ada state global yang diubah; cleanup tidak diperlukan karena spec hanya membaca.

## Test Steps

### TC-FA-TAG-31: Klik kartu Reported memfilter tabel grup ke baris dengan nilai lebih dari nol

1. Klik kartu `Reported`
2. Verifikasi kartu `Reported` aktif dengan penanda terpilih
3. Verifikasi tabel grup hanya memuat Excavator 20 Ton / Plant B dan Laptop Pro 14 / HQ
4. Verifikasi dua kartu lain tidak aktif

### TC-FA-TAG-32: Klik ulang kartu Reported yang aktif membersihkan filter

5. Klik kartu `Reported` sekali lagi
6. Verifikasi kartu `Reported` tidak aktif
7. Verifikasi empat baris grup tampil kembali

### TC-FA-TAG-33: Klik kartu Non-standard memfilter tabel grup ke baris dengan nilai lebih dari nol

8. Klik kartu `Non-standard`
9. Verifikasi kartu `Non-standard` aktif dengan penanda terpilih
10. Verifikasi tabel grup hanya memuat Excavator 20 Ton / Plant B dan Forklift Manual / Plant A
11. Verifikasi dua kartu lain tidak aktif

### TC-FA-TAG-34: Klik ulang kartu Non-standard yang aktif membersihkan filter

12. Klik kartu `Non-standard` sekali lagi
13. Verifikasi kartu `Non-standard` tidak aktif
14. Verifikasi empat baris grup tampil kembali

### TC-FA-TAG-35: Klik kartu Not Paired Yet memfilter tabel grup ke baris dengan nilai lebih dari nol

15. Klik kartu `Not Paired Yet`
16. Verifikasi kartu `Not Paired Yet` aktif dengan penanda terpilih
17. Verifikasi tabel grup hanya memuat Excavator 20 Ton / Plant A dan Laptop Pro 14 / HQ
18. Verifikasi dua kartu lain tidak aktif

### TC-FA-TAG-36: Klik ulang kartu Not Paired Yet yang aktif membersihkan filter

19. Klik kartu `Not Paired Yet` sekali lagi
20. Verifikasi kartu `Not Paired Yet` tidak aktif
21. Verifikasi empat baris grup tampil kembali

### TC-FA-TAG-37: Hanya satu kartu aktif pada satu waktu

22. Klik kartu `Reported`
23. Klik kartu `Non-standard`
24. Verifikasi hanya kartu `Non-standard` aktif
25. Verifikasi kartu `Reported` kembali tidak aktif
26. Verifikasi tabel grup memuat Excavator 20 Ton / Plant B dan Forklift Manual / Plant A
27. Klik kartu `Non-standard` untuk membersihkan filter

### TC-FA-TAG-38: Klik kartu Not Paired Yet membuat Popup Detail hanya memuat aset Not Paired Yet

28. Klik kartu `Not Paired Yet`
29. Klik Asset Name `Excavator 20 Ton` pada baris Plant A
30. Verifikasi Popup Detail terbuka dengan judul `Assets`
31. Verifikasi tabel T-TAG-02 hanya memuat dua aset Not Paired Yet
32. Verifikasi kolom TAG Code `—` dan Status `Not Paired Yet` pada kedua aset
33. Tutup popup dengan ikon close
34. Klik kartu `Not Paired Yet` untuk membersihkan filter

## Notes

- Langkah 27, 33, dan 34 adalah langkah penghubung (membersihkan filter kartu; menutup popup), tanpa asersi (S-03, S-09).
- Langkah 1 TC-FA-TAG-32, 34, dan 36 (klik kartu untuk pertama kali) identik dengan langkah 1 TC-FA-TAG-31, 33, dan 35 dan sudah dijalankan pada langkah 1, 8, dan 15; kartu tetap aktif sampai TC berikutnya sehingga langkah 5, 12, dan 19 hanya memuat klik kedua. Urutan TC tidak diubah.
- Langkah 4, 11, dan 18 memuat klausa "dua kartu lain tidak aktif" sebagai asersi absence atas state kartu; anchor positif adalah Verifikasi kartu terpilih aktif pada langkah sebelumnya (langkah 2, 9, 16) (bagian 8b butir 2).
- TC-FA-TAG-39 sampai 41 ada di spec 008.
- Temuan untuk QA:
  - TC-FA-TAG-38 tidak menyebut nama atau ID kedua aset Not Paired Yet milik grup Excavator 20 Ton / Plant A; spec hanya mengasersi jumlah dan nilai kolom TAG Code serta Status.
  - Nama dan kode literal Pre-setup tidak diberi suffix karena TC menuntut asersi nama, urutan, dan jumlah, sedangkan konvensi (S-06, S-12) hanya mengizinkannya lewat Lampiran A yang belum memuat butir modul ini. Spec hanya membaca data itu.
