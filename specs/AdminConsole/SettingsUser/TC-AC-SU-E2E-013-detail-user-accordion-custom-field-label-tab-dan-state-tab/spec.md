---
id: TC-AC-SU-E2E-013-detail-user-accordion-custom-field-label-tab-dan-state-tab
title: "Detail User: Accordion Custom Field, Label Tab Responsibilities, State Tab, dan Breadcrumb Mempertahankan State List"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-38
  - TC-AC-SU-46
  - TC-AC-SU-48
  - TC-AC-SU-49
coverage:
  web: automated
---

# Detail User: Accordion Custom Field, Label Tab Responsibilities, State Tab, dan Breadcrumb Mempertahankan State List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-38, 49 | `Jane Smith` | `Jane Smith {runId}-013` | `janesmith+{runId}-013@qwertysystem.net` | Activated, Active; sedikitnya 2 entri Changelog, dengan sedikitnya satu entri yang memuat kata `Assign` |
| TC-AC-SU-46 | `John Doe` | `John Doe {runId}-013` | `johndoe+{runId}-013@qwertysystem.net` | Activated, Active; nilai `Blood Type {runId}-013` = `O`, `Emergency Phone {runId}-013` = `+62 81234567890` |
| TC-AC-SU-48 | `Dewi Lestari` | `Dewi Lestari {runId}-013` | `dewilestari+{runId}-013@qwertysystem.net` | approver-eligible untuk 3 request Waiting for Approval |
| TC-AC-SU-48 | `Sarah Lee` | `Sarah Lee {runId}-013` | `sarahlee+{runId}-013@qwertysystem.net` | 0 request Waiting for Approval |
| TC-AC-SU-46 | Custom Field `Blood Type` | `Blood Type {runId}-013` | - | Dropdown, aktif; opsi `O` |
| TC-AC-SU-46 | Custom Field `Emergency Phone` | `Emergency Phone {runId}-013` | - | Phone, aktif |

- Data user lain di entitas (>10 baris, Pre-setup) dipakai TC-AC-SU-38; Custom Field seed dihapus di hook `after`. Seeding entri Changelog dan request Waiting for Approval lewat Fixture BE (disediakan tim FE/BE).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-38: Breadcrumb Detail User segmen User kembali ke List dengan state dipertahankan

1. Ketik Search `Jane`, tekan Enter
2. Klik header kolom Email untuk mengurutkan ascending
3. Klik Name `Jane Smith {runId}-013`
4. Klik segmen `User` pada Breadcrumb
5. Verifikasi kembali ke Settings > User
6. Verifikasi keyword `Jane` tetap di kotak Search
7. Verifikasi tabel menampilkan sedikitnya satu baris hasil Search
8. Verifikasi hasil tetap tersaring oleh keyword `Jane`
9. Verifikasi sort Email ascending tetap aktif
10. Klik Settings > User di sidebar untuk mereset Search dan Sort

### TC-AC-SU-46: Accordion Custom Field expand dan collapse

11. Ketik Search `John Doe {runId}-013`, tekan Enter
12. Klik Name `John Doe {runId}-013`
13. Verifikasi awal: hanya header `Custom Field` dengan icon `▶`
14. Klik header `Custom Field`
15. Verifikasi icon `▼`
16. Verifikasi tampil key-value read-only `Blood Type {runId}-013: O`
17. Verifikasi tampil key-value read-only `Emergency Phone {runId}-013: +62 81234567890`
18. Klik header `Custom Field` lagi
19. Verifikasi accordion `Custom Field` kembali collapsed
20. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-48: Label Tab Responsibilities menampilkan jumlah

21. Ganti isi kotak search dengan `Dewi Lestari {runId}-013`, tekan Enter
22. Klik Name `Dewi Lestari {runId}-013`
23. Verifikasi label tab `Responsibilities (3)` pada Detail `Dewi Lestari {runId}-013`
24. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
25. Ganti isi kotak search dengan `Sarah Lee {runId}-013`, tekan Enter
26. Klik Name `Sarah Lee {runId}-013`
27. Verifikasi label tab `Responsibilities (0)` pada Detail `Sarah Lee {runId}-013`
28. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-49: Pindah tab Detail User tidak mereset state tab lain

29. Ganti isi kotak search dengan `Jane Smith {runId}-013`, tekan Enter
30. Klik Name `Jane Smith {runId}-013`
31. Klik Tab Changelog
32. Ketik Search `Assign`, tekan Enter
33. Klik Tab Role
34. Klik sub-tab Group Role
35. Klik Tab Changelog
36. Verifikasi keyword `Assign` tetap di kotak Search Tab Changelog
37. Verifikasi hasil `Assign` tetap tampil di Tab Changelog
38. Klik Tab Role
39. Verifikasi sub-tab Group Role tetap aktif
40. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
41. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), langkah 10 (reset Search dan Sort lewat klik sidebar), langkah 20, 40, dan kembali ke daftar lainnya, langkah 41 (reset Search).
- Ukuran spec (41 langkah, di atas smell sekitar 35 langkah): empat blok TC pada halaman List dan Detail yang sama dengan seed terpisah per blok; tiap blok berdiri sendiri (dimulai dan diakhiri di List) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-38: keyword `Jane` memuat juga user Pre-setup `Jane Smith`; spec mengklik baris `Jane Smith {runId}-013`. Data bervariasi >10 baris dipenuhi oleh data Pre-setup.
  - TC-AC-SU-46: Custom Field `Blood Type` dan `Emergency Phone` tidak ada di Tabel Pre-setup; spec membuatnya bersuffix `{runId}-013` lewat Fixture BE, sehingga key-value diasersi dengan nama bersuffix.
  - TC-AC-SU-48: mekanisme membuat "3 request Waiting for Approval" dengan `Dewi Lestari` sebagai approver-eligible tidak dijelaskan TC; disediakan tim FE/BE.
  - TC-AC-SU-49: TC hanya mensyaratkan "≥2 entri Changelog" dan men-Search `Assign`; spec men-seed sedikitnya satu entri yang memuat `Assign` agar hasil Search tidak kosong.
  - Nama user TC (`Jane Smith`, `John Doe`, `Dewi Lestari`, `Sarah Lee`) dipakai sebagai nama bersuffix `{runId}-013` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
