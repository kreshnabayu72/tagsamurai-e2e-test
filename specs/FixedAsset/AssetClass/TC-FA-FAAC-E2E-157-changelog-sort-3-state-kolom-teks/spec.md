---
id: TC-FA-FAAC-E2E-157-changelog-sort-3-state-kolom-teks
title: "Modal Changelog: Sort Tiga Tahap pada Kolom Teks Action, Class Code, Field, dan Modified By"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-500
sourceRules: ["§4.1.1#r27", "§4.4#r14", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r32", "§4.1.1#r26"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r27": 4
  "§4.4#r14": [6, 8, 12, 14, 18, 20, 24, 26]
  "§4.1.1#r28": 10
  "§4.1.1#r29": 16
  "§4.1.1#r32": 22
  "§4.1.1#r26": 27
coverage:
  web: automated
---

# Modal Changelog: Sort Tiga Tahap pada Kolom Teks Action, Class Code, Field, dan Modified By

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Parameter urutan kolom TC-500 (nilai distinct pada 19 entri): Action (Create, Delete, Edit), Class Code (HEAVY-EQ, IT-EQ, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, TEMP-EQ, VEHICLES), Field (Asset Names, Class Code, Class Name, Declining Rate, Last Exported Period, Last Posted Period, Scheduled Version, Status, Useful Life), Modified By (Budi S, Rina P, System).
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog
2. Ubah ukuran halaman ke 25 agar seluruh entri tampil pada satu halaman

### TC-FA-FAAC-500: Sort tiga tahap pada kolom teks Action, Class Code, Field, dan Modified By

3. Klik header `Action` satu kali
4. Verifikasi Action klik 1: A-Z (`Create`, `Delete`, lalu `Edit`)
5. Klik header `Action` kedua kali
6. Verifikasi Action klik 2: Z-A (`Edit`, `Delete`, lalu `Create`)
7. Klik header `Action` ketiga kali
8. Verifikasi indikator sort `Action` netral
9. Klik header `Class Code` satu kali
10. Verifikasi Class Code klik 1: A-Z tanpa membedakan huruf besar-kecil (HEAVY-EQ, IT-EQ, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, TEMP-EQ, VEHICLES)
11. Klik header `Class Code` kedua kali
12. Verifikasi Class Code klik 2: Z-A (urutan kebalikan klik 1)
13. Klik header `Class Code` ketiga kali
14. Verifikasi indikator sort `Class Code` netral
15. Klik header `Field` satu kali
16. Verifikasi Field klik 1: A-Z (Asset Names, Class Code, Class Name, Declining Rate, Last Exported Period, Last Posted Period, Scheduled Version, Status, Useful Life)
17. Klik header `Field` kedua kali
18. Verifikasi Field klik 2: Z-A (urutan kebalikan klik 1)
19. Klik header `Field` ketiga kali
20. Verifikasi indikator sort `Field` netral
21. Klik header `Modified By` satu kali
22. Verifikasi Modified By klik 1: A-Z (Budi S, Rina P, System)
23. Klik header `Modified By` kedua kali
24. Verifikasi Modified By klik 2: Z-A (urutan kebalikan klik 1)
25. Klik header `Modified By` ketiga kali
26. Verifikasi indikator sort `Modified By` netral
27. Verifikasi entri bernilai sama mengikuti default sort Date Newest First

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. Ukuran halaman diubah ke 25 pada langkah 2 (langkah penghubung, S-14) supaya seluruh 19 entri teramati pada satu halaman; TC tidak menyebut ukuran halaman.
5. Klik 3 pada tiap kolom mengembalikan sort ke netral sehingga kolom berikutnya mulai dari default (S-09). Asersi terakhir (entri bernilai sama mengikuti default sort Date Newest First) diamati sesudah klik ketiga kolom Modified By.
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 2.
