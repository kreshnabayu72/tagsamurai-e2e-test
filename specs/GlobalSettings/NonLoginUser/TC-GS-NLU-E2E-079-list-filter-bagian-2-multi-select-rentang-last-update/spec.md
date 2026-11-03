---
id: TC-GS-NLU-E2E-079-list-filter-bagian-2-multi-select-rentang-last-update
title: "List Filter bagian 2: dropdown multi-select, rentang Last Update inklusif, field curated Temporary User, Temporary Until, Custom Field, dan range Numeric"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-269
  - TC-GS-NLU-270
  - TC-GS-NLU-271
  - TC-GS-NLU-468
coverage:
  web: automated
---

# List Filter bagian 2: dropdown multi-select, rentang Last Update inklusif, field curated Temporary User, Temporary Until, Custom Field, dan range Numeric

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1; `{namaCompany}` diisi sesuai Client uji). Login sekali di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password lewat `Spectra.env.GS_TC_PASSWORD`, tidak ditulis di spec atau fixture.
- Layar awal: Global Settings > User > User List > sub-tab Non-Login User, dibuka hook `beforeEach` suite.
- Data Pre-setup (No. 9 sampai 13; hanya dibaca, tidak diubah, tanpa suffix): Non-Login User `Budi Kurniawan` (Field Technician, Operations, Represented By Ahmad Fauzi, Active), `Rina Marlina` (Driver, Logistics, Temporary +30 hari, Blood Type `O`), `Joko Susilo` dan `Agus Salim` (Contractor, Inactive); Custom Field dasar `Blood Type` (Dropdown A/B/O/AB, Active). Kolom Temporary User, Temporary Until, dan Blood Type berstatus Hidden (default) selama spec ini. Fixture baru `Fixture.nonLoginUser.preSetup` (belum ada).
- Data Dinamis (di-seed hook `before` lewat API, mekanisme disediakan tim FE/BE; dihapus hook `after`): Custom Field `Skor Uji` (Numeric, 0 desimal, Active; sisa field bernama sama dari run sebelumnya dibersihkan hook `before`); Non-Login User `Skor Delapan Puluh {runId}-079` (nilai `Skor Uji` `80`) dan `Skor Enam Puluh {runId}-079` (nilai `60`), masing-masing Division `Operations`, Represented By `Ahmad Fauzi`, Active. Dipakai TC-GS-NLU-468 menggantikan `Budi Kurniawan` dan `Siti Rahayu` agar Pre-setup tidak diubah (S-06).
- Tanggal Last Update `Budi Kurniawan` dibaca dari sel tabel pada TC-GS-NLU-270; tanggal Temporary Until `Rina Marlina` (hari seeding + 30 hari) dibaca lewat kemampuan baca data yang disediakan tim FE/BE.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-non-login-user` true untuk akun Total Control dan hook suite `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: pengisian date picker rentang; pengamatan placeholder `Min` dan `Max`.
- State global: tidak ada yang diubah selain Custom Field `Skor Uji` (dibuat dan dihapus hook). State Filter dibersihkan oleh langkah penghubung. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-NLU-269: Filter dropdown multi-select Active, Position, Division, dan Represented By

1. Buka Filter Panel, pilih Active `Inactive`, klik `[Apply]`
2. Verifikasi hanya baris Inactive yang tampil: baris `Joko Susilo` dan `Agus Salim` tampil dan seluruh baris hasil berstatus Inactive
3. Buka Filter Panel, klik `[Clear Field]`, pilih Position `Driver` dan `Contractor`, klik `[Apply]`
4. Verifikasi hanya baris Position `Driver` atau `Contractor` yang tampil (logika OR dalam field): sedikitnya satu baris tampil dan seluruh baris hasil ber-Position `Driver` atau `Contractor`
5. Buka Filter Panel, klik `[Clear Field]`, pilih Division `Operations`, klik `[Apply]`
6. Verifikasi baris Division `Operations` tampil: sedikitnya satu baris tampil dan seluruh baris hasil ber-Division `Operations`
7. Buka Filter Panel, klik `[Clear Field]`, pilih Represented By `Ahmad Fauzi`, klik `[Apply]`
8. Verifikasi baris yang diwakili `Ahmad Fauzi` tampil: sedikitnya satu baris tampil dan seluruh baris hasil ber-Represented By `Ahmad F`

### TC-GS-NLU-270: Filter Last Update menggunakan rentang tanggal inklusif

9. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`
10. Ketik Search `Budi Kurniawan`, tekan Enter, catat tanggal sel Last Update baris `Budi Kurniawan`, klik `(←)` pada kotak Search
11. Buka Filter Panel dan amati field Last Update
12. Verifikasi placeholder date picker `Select date`
13. Pilih rentang tanggal satu hari (Start = End) yang memuat Last Update `Budi Kurniawan`
14. Verifikasi tanggal terformat sesuai General Settings (`dd/MM/yy`)
15. Klik `[Apply]`
16. Verifikasi baris `Budi Kurniawan` tampil (batas inklusif: Last Update pada hari tersebut)

### TC-GS-NLU-271: Filter field curated Temporary User, Temporary Until, dan Custom Field aktif

17. Buka Filter Panel, klik `[Clear Field]`
18. Verifikasi field curated muncul di Filter Panel walau kolomnya Hidden: placeholder `All options` (Temporary User), `Select date` (Temporary Until), `All blood types` (Blood Type)
19. Pilih Temporary User `Yes`, klik `[Apply]`
20. Verifikasi hanya baris Temporary User yang tampil: baris `Rina Marlina` tampil dan seluruh baris hasil bertipe Temporary User
21. Buka Filter Panel, klik `[Clear Field]`, pilih rentang Temporary Until yang memuat tanggal `Rina Marlina`, klik `[Apply]`
22. Verifikasi baris dalam rentang Temporary Until tampil: baris `Rina Marlina` tampil
23. Buka Filter Panel, klik `[Clear Field]`, pilih Blood Type `O`, klik `[Apply]`
24. Verifikasi baris Blood Type `O` tampil: baris `Rina Marlina` tampil dan seluruh baris hasil ber-Blood Type `O`

### TC-GS-NLU-468: Filter range Custom Field Numeric memakai Min dan Max inklusif

25. Buka Filter Panel, klik `[Clear Field]`
26. Verifikasi field `Skor Uji` menampilkan dua input dengan placeholder `Min` dan `Max`
27. Verifikasi field `Skor Uji` tersedia walau kolomnya Hidden (kolom `Skor Uji` tidak ada di header tabel)
28. Isi `Min` `70`, isi `Max` `90`, klik `[Apply]`
29. Verifikasi hanya record bernilai `Skor Uji` `80` yang tampil (`Skor Delapan Puluh {runId}-079` tampil, `Skor Enam Puluh {runId}-079` tidak tampil)
30. Buka Filter Panel, ubah `Min` `80`, ubah `Max` `80`, klik `[Apply]`
31. Verifikasi batas inklusif: hanya record bernilai `Skor Uji` `80` yang tampil (`Skor Delapan Puluh {runId}-079` tampil, `Skor Enam Puluh {runId}-079` tidak tampil)
32. Buka Filter Panel, klik `[Clear Field]`, klik `[Apply]`

## Notes

- Langkah penghubung (S-03): membuka Filter Panel dan `[Clear Field]` sebelum tiap langkah TC (TC tidak menyebut Filter dibersihkan antar langkah, supaya tiap Expected menguji satu field), Search `Budi Kurniawan` untuk menemukan baris target dan mencatat tanggal Last Update (R-16), `(←)` yang mengosongkan Search, dan langkah akhir yang membersihkan Filter. Asumsi dari TC-GS-NLU-274 dan TC-GS-NLU-275: `[Apply]` menutup Filter Panel.
- Asersi tambahan (S-03): placeholder `Select date` pada TC-GS-NLU-270 dan format tanggal sebelum Apply mengikuti Expected b TC yang sama; baris pembanding `Rina Marlina` menjadi anchor asersi universal (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-NLU-269 tidak menyebut apakah filter langkah sebelumnya dibersihkan; bila kumulatif, Expected d tidak dapat terpenuhi untuk baris yang tidak memenuhi filter sebelumnya. Spec membersihkan filter tiap langkah.
  - TC-GS-NLU-270 dan TC-GS-NLU-271 tidak menyebut cara mendapatkan tanggal Last Update `Budi Kurniawan` dan tanggal Temporary Until `Rina Marlina` (Pre-setup hanya menyebut "+30 hari").
  - TC-GS-NLU-271 langkah 1 meminta kolom curated tidak diaktifkan; kondisi itu hanya dijamin bila tidak ada spec lain yang meninggalkan preferensi kolom di browser (dipulihkan hook `after` spec lain).
  - TC-GS-NLU-468 precondition d memakai nilai `Skor Uji` pada `Budi Kurniawan` (`80`) dan `Siti Rahayu` (`60`); spec memakai record milik sendiri agar Pre-setup tidak ditulis, dan nama literal Custom Field `Skor Uji` mengikuti TC (Lampiran A tidak memuat pengecualian S-12 untuk modul ini; `suite.md` menyatakan field uji dibuat dan dibersihkan hook).
