---
id: TC-GS-ROLE-E2E-063-detail-filter-panel-screening-dan-per-field
title: "Detail Manage TAG: Screening Panel Filter dan Filter per Field serta Kombinasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-189
  - TC-GS-ROLE-190
coverage:
  web: automated
---

# Detail Manage TAG: Screening Panel Filter dan Filter per Field serta Kombinasi

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; seluruh data hanya dibaca.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > System > Detail "Manage TAG" dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Detail "Manage TAG" berisi sedikitnya 4 user dengan Position dan Division berbeda (precondition TC) dengan nilai berbeda pada tiap kolom yang difilter: Position (mis. `Staff`, `Finance Staff`, `HR Manager`), Division (mis. `IT`, `Finance`, `HR`), Activation Status (`Activated` dan `Pending Activation`), Temporary User (`Yes` dan `No`), Temporary Until (tanggal berbeda), dan Custom Field aktif `Region` (sedikitnya satu user bernilai `Bandung`). Keberadaan nilai-nilai ini pada Detail "Manage TAG" mengikuti TC dan disediakan tim FE. Custom Field aktif `Region` disediakan tim FE.
- Tabel "Filter tunggal" untuk TC-GS-ROLE-190 (satu Filter per iterasi, dikosongkan sebelum iterasi berikutnya):

  | Field | Nilai | Kriteria setiap baris hasil |
  |---|---|---|
  | Position | `Staff` | Position bernilai `Staff` |
  | Division | `IT` | Division bernilai `IT` |
  | Activation Status | `Activated` | Activation Status bernilai `Activated` |
  | Temporary User | `No` | Temporary User bernilai `No` |
  | Temporary Until | rentang `{rentang Temporary Until}` | Temporary Until berada di dalam rentang |

- Data uji: `{rentang Temporary Until}` adalah rentang tanggal yang memuat sedikitnya satu tanggal Temporary Until user pada Detail "Manage TAG" (ditulis dalam format tanggal General Settings aktif, dibaca di hook `before` lewat kemampuan membaca data yang disediakan tim FE). Kombinasi: Division `IT` dan Activation Status `Activated`. Custom Field: `Region` bernilai `Bandung`.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3). Kolom `Activation Status`, `Temporary User`, `Temporary Until`, dan `Region` default tersembunyi dan ditampilkan lewat langkah 10 sampai 13 agar nilai tiap baris hasil Filter dapat diasersi.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Detail "Manage TAG" dikembalikan ke default (kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region` tersembunyi) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel itu di browser (langkah 40 sampai 43); Filter dikosongkan oleh langkah di spec dan hook `beforeEach`.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System > Detail "Manage TAG".
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca data Temporary Until per user (disediakan tim FE); membaca dan menghapus preferensi kolom di penyimpanan browser; memilih rentang tanggal pada date range picker.

## Test Steps

### TC-GS-ROLE-189: Screening Filter Panel Detail

1. Klik Filter
2. Verifikasi field Position menampilkan `All positions`
3. Verifikasi field Division menampilkan `All divisions`
4. Verifikasi field Activation Status menampilkan `All statuses`
5. Verifikasi field Temporary User menampilkan `All options` (multi-select searchable)
6. Verifikasi field Temporary Until menampilkan `Select date` (date range picker)
7. Verifikasi field Custom Field `Region` tampil sesuai tipe field
8. Verifikasi panel Filter tidak memuat field Status, Modified By, dan Last Updated
9. Tekan Esc untuk menutup panel Filter

### Persiapan kolom

10. Klik header kolom Column Visibility (⋯)
11. Klik item `Setup Column...`
12. Centang `Activation Status`, `Temporary User`, `Temporary Until`, dan `Region`
13. Klik `[Save]`

### TC-GS-ROLE-190: Filter Detail per field dan kombinasi

Untuk setiap baris tabel "Filter tunggal" (langkah 14 sampai 21):
14. Klik Filter
15. Pilih field sesuai baris tabel dengan nilai sesuai baris tabel
16. Klik `[Apply]`
17. Verifikasi tabel memuat sedikitnya satu baris hasil
18. Verifikasi setiap baris hasil memenuhi kriteria sesuai baris tabel
19. Klik Filter
20. Klik `[Clear Field]`
21. Klik `[Apply]`
22. Klik Filter
23. Pilih Division `IT`
24. Pilih Activation Status `Activated`
25. Klik `[Apply]`
26. Verifikasi tabel memuat sedikitnya satu baris hasil
27. Verifikasi setiap baris hasil memiliki Division `IT`
28. Verifikasi setiap baris hasil memiliki Activation Status `Activated`
29. Klik Filter
30. Klik `[Clear Field]`
31. Klik `[Apply]`
32. Klik Filter
33. Pilih Custom Field `Region` dengan nilai `Bandung`
34. Klik `[Apply]`
35. Verifikasi tabel memuat sedikitnya satu baris hasil
36. Verifikasi setiap baris hasil memiliki Region `Bandung`
37. Klik Filter
38. Klik `[Clear Field]`
39. Klik `[Apply]`

### Pemulihan kolom

40. Klik header kolom Column Visibility (⋯)
41. Klik item `Setup Column...`
42. Klik `[Reset to Default]`
43. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (data Detail dimuat dari backend nyata; Filter bekerja terhadap data server).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (189, 190) dipertahankan. Blok "Persiapan kolom" dan "Pemulihan kolom" adalah langkah penghubung (aksi tanpa `Verifikasi`).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah "Tekan Esc untuk menutup panel Filter" di akhir TC-GS-ROLE-189 (menutup panel sebelum iterasi pertama TC-GS-ROLE-190), langkah 10 sampai 13 (menampilkan kolom yang nilainya diasersi), dan langkah 40 sampai 43 (mengembalikan konfigurasi default; hook `after` sebagai cadangan). Tiga langkah penutup tiap Filter ("Klik Filter", `[Clear Field]`, `[Apply]`) mengosongkan Filter sebelum Filter berikutnya.
- Langkah 14 sampai 21 diulang untuk lima baris tabel "Filter tunggal" (8 langkah, 40 setelah ekspansi). Asersi universal ("setiap baris hasil") didahului `Verifikasi` yang membuktikan tabel memuat sedikitnya satu baris hasil.
- Spec melewati sekitar 35 langkah (43 langkah nominal, 75 setelah ekspansi) karena dua TC memakai tabel Detail "Manage TAG" yang sama dan satu kelas harness (fungsional, tanpa data tulis); TC-GS-ROLE-190 menguji lima field tunggal, satu kombinasi, dan satu Custom Field sesuai langkah TC. Tiap Filter dikosongkan sebelum Filter berikutnya, sehingga kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna, dan blok screening (TC-GS-ROLE-189) berdiri sendiri.
- Pembagian TC lintas spec: TC-GS-ROLE-186 sampai 188 (Search Detail) di spec 062; Download Detail (TC-GS-ROLE-194 dan 303) di spec 061.
- Temuan untuk QA:
  - TC-GS-ROLE-190: TC tidak menyebut bahwa kolom `Activation Status`, `Temporary User`, `Temporary Until`, dan `Region` harus ditampilkan agar hasil Filter dapat diamati (default tersembunyi); spec menampilkannya lewat Setup Column sebagai langkah penghubung.
  - TC-GS-ROLE-190 langkah 1 menyebut "catat" tanpa menyebut apa yang dicatat; spec mengasersi kriteria setiap baris hasil. Langkah 5 menyebut "rentang tertentu" tanpa nilai; spec memakai rentang yang disediakan tim FE.
  - TC-GS-ROLE-189 Expected a: TC tidak menyebut placeholder field Custom Field; spec mengasersi field `Region` tampil sesuai tipe field.
  - TC-GS-ROLE-190: "Clear" ditulis sebagai `[Clear Field]` lalu `[Apply]` mengikuti pola TC-GS-ROLE-157 dan 158.
