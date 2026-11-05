---
id: TC-FA-FAAC-E2E-147-changelog-search-action-field-class-code-old-new-value
title: "Modal Changelog: Search pada Kolom Action, Field, Class Code, Old Value, dan New Value"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-477
  - TC-FA-FAAC-478
  - TC-FA-FAAC-479
  - TC-FA-FAAC-480
coverage:
  web: automated
---

# Modal Changelog: Search pada Kolom Action, Field, Class Code, Old Value, dan New Value

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Seed relatif terhadap tanggal run: entri Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 memakai New Value bulan M+2 (bulan berjalan ditambah dua bulan, format MMM yyyy); fixture BE membuat seed ini relatif terhadap tanggal run, dan spec tidak menulis nama bulan literal (kata kunci Search TC-FA-FAAC-479 adalah bulan M+2 itu); bulan berjalan dan M+2 dihitung pada zona waktu General Settings client (NC-11).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog
2. Verifikasi tabel modal memuat sedikitnya satu baris entri

### TC-FA-FAAC-477: Search pada kolom Action dan Field

3. Ketik Search `creat` di modal, tekan Enter
4. Verifikasi tabel menampilkan dua entri Create (HEAVY-EQ dan IT-EQ, 05/08/26)
5. Klik `✕` pada kotak Search di modal, tekan Enter
6. Ketik Search `DELETE` di modal, tekan Enter
7. Verifikasi tabel menampilkan satu entri Delete (TEMP-EQ)
8. Klik `✕` pada kotak Search di modal, tekan Enter
9. Ketik Search `declining` di modal, tekan Enter
10. Verifikasi tabel menampilkan entri Declining Rate IT-EQ
11. Klik `✕` pada kotak Search di modal, tekan Enter
12. Ketik Search `scheduled` di modal, tekan Enter
13. Verifikasi tabel menampilkan entri Scheduled Version HEAVY-EQ
14. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-478: Search pada kolom Class Code

15. Ketik Search `machinery` di modal, tekan Enter
16. Verifikasi tabel menampilkan dua entri MACHINERY (Class Code dan Class Name, 30/09/26 16:20)
17. Klik `✕` pada kotak Search di modal, tekan Enter
18. Ketik Search `TEMP-EQ` di modal, tekan Enter
19. Verifikasi tabel menampilkan satu entri Delete TEMP-EQ
20. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-479: Search pada kolom Old Value dan New Value

21. Ketik Search `it equipments` di modal, tekan Enter
22. Verifikasi Old Value: tabel menampilkan entri Class Name IT-EQ (dari `IT Equipments` menjadi `IT Equipment`)
23. Klik `✕` pada kotak Search di modal, tekan Enter
24. Ketik Search bulan M+2 dalam format MMM yyyy, dihitung pada zona waktu General Settings client (lihat Prerequisites), di modal, tekan Enter
25. Verifikasi New Value: tabel menampilkan entri Scheduled Version HEAVY-EQ
26. Klik `✕` pada kotak Search di modal, tekan Enter
27. Ketik Search `48` di modal, tekan Enter
28. Verifikasi tabel menampilkan entri Useful Life IT-EQ (dari 48 menjadi 60)
29. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-480: Search `active` pada Old Value dan New Value juga mencocokkan Inactive

30. Ketik Search `active` di modal, tekan Enter
31. Verifikasi tabel menampilkan entri Status OFFICE-NEW (dari `Inactive` menjadi `Active`) dan entri Status OFFICE-OLD (dari `Active` menjadi `Inactive`)
32. Verifikasi nilai `Inactive` dihitung cocok karena pencocokan substring tidak membedakan huruf besar-kecil
33. Klik `✕` pada kotak Search di modal, tekan Enter

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. Langkah 'Klik ✕ lalu tekan Enter pada input kosong' di antara pencarian TC-477, TC-478, dan TC-479 adalah langkah TC; langkah yang sama di akhir tiap blok adalah langkah penghubung yang mengosongkan Search sebelum blok berikutnya (S-09). Pembanding generik untuk hasil Search adalah `Verifikasi` langkah 2.
5. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 14, 20, 29, 33.
