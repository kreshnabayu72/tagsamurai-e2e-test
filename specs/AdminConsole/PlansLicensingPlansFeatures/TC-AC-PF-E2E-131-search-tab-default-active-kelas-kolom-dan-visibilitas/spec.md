---
id: TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas
title: Search Tab Default Active Kelas Kolom dan Visibilitas Kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-304
  - TC-AC-PF-305
  - TC-AC-PF-306
  - TC-AC-PF-307
  - TC-AC-PF-308
coverage:
  web: automated
---

# Search Tab Default Active Kelas Kolom dan Visibilitas Kolom

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter` (FAMS, Free, v2, Clients 12, Last Modified 15 Jun 26), `Growth` (FAMS, Paid, v5, 47, 15 Jun 26), `Professional` (FAMS, Paid, v3, 23, 15 Jun 26), `Enterprise` (FAMS, Paid, v1, 8, 12 Aug 26), `SIEM` (SIEM, Paid, v1, 5, 09 Jul 26).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: visibilitas kolom `Product` disembunyikan lalu dipulihkan di dalam spec (langkah 16 dan 19); preferensi kolom browser dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-304 Kelas teks Plan Name

1. Ketik Search `PROF`, tekan Enter.
2. Verifikasi tabel menampilkan baris `Professional` saja.
3. Ganti isi kotak search dengan `ent`, tekan Enter.
4. Verifikasi tabel menampilkan baris `Enterprise` saja (substring pada Plan Name).

### TC-AC-PF-305 Kelas badge Product dan Pricing Type

5. Ganti isi kotak search dengan `free`, tekan Enter.
6. Verifikasi `free` (Pricing Type) menampilkan baris `Starter`.
7. Ganti isi kotak search dengan `siem`, tekan Enter.
8. Verifikasi `siem` (Product dan Plan Name) menampilkan baris `SIEM`.

### TC-AC-PF-306 Kelas angka Version dan Clients

9. Ganti isi kotak search dengan `5`, tekan Enter.
10. Verifikasi tabel menampilkan baris `Growth` (Version `v5`) dan `SIEM` (Clients `5`).

### TC-AC-PF-307 Kolom tanggal tidak dicocokkan

11. Kosongkan isi kotak search, tekan Enter.
12. Verifikasi baris `Starter`, `Growth`, dan `Professional` tampil dengan Last Modified `15 Jun 26`.
13. Ganti isi kotak search dengan `Jun`, tekan Enter.
14. Verifikasi tabel menampilkan empty state "No results found".
15. Kosongkan isi kotak search, tekan Enter.

### TC-AC-PF-308 Search terikat visibilitas kolom

16. Sembunyikan kolom `Product` lewat Overlay Column Visibility.
17. Ketik Search `FAMS`, tekan Enter.
18. Verifikasi Search `FAMS` menampilkan "No results found" saat kolom `Product` tersembunyi.
19. Tampilkan kembali kolom `Product` lewat Overlay Column Visibility.
20. Tekan Enter pada kotak Search yang masih berisi `FAMS`.
21. Verifikasi tabel menampilkan empat baris FAMS (`Starter`, `Growth`, `Professional`, `Enterprise`).
22. Kosongkan isi kotak search, tekan Enter.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 11 dan 15 mengosongkan Search; langkah 22 mengosongkan Search di akhir spec; langkah 20 menjalankan ulang Search `FAMS` pada kotak yang masih berisi kata kunci itu ("Jalankan Search `FAMS` lagi" di TC-AC-PF-308).
- Anchor absence (bagian 8b butir 2): "No results found" pada langkah 14 dan 18 didahului langkah 12 (baris yang sama tampil di tabel tanpa Search).
- Temuan untuk QA: TC-AC-PF-307 menyebut tiga baris ber-Last Modified `15 Jun 26` hanya sebagai penjelasan Expected; spec mengasersinya sebagai anchor positif (langkah 12).
