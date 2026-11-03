---
id: TC-GS-NLU-E2E-112-absence-log-edit-tanpa-perubahan-import-dan-delete-login
title: "Absence log: Edit tanpa perubahan, Import, dan Delete Login User pointer"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-182
  - TC-GS-NLU-183
  - TC-GS-NLU-425
  - TC-GS-NLU-469
coverage:
  web: automated
---

# Absence log: Edit tanpa perubahan, Import, dan Delete Login User pointer

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`) hanya dibaca, tidak diubah atau dihapus.
- Spec absence (kelas g): tiap TC memakai record dan baseline sendiri; pemicu hanya membentuk kondisi yang diasersi tidak tercatat.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - TC-GS-NLU-182: `Edit Nol {runId}-112` (First Name `Edit`, Last Name `Nol {runId}-112`, Division `Operations`, Email `editnol+{runId}-112@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active).
  - TC-GS-NLU-183: `Edit Besar {runId}-112` (First Name `Edit`, Last Name `Besar {runId}-112`, Division `Operations`, Employee ID `EDT-{runId}-0112`, Email `editbesar+{runId}-112@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active).
  - TC-GS-NLU-425: `Impor Dua {runId}-112` dibuat lewat Import "User Non Login" (job Import selesai); mekanisme menjalankan Import di hook `before` disediakan tim FE/BE (lihat Temuan untuk QA).
  - TC-GS-NLU-469: Login User `Wawan Pointer {runId}-112` (Active, Manager, Warehouse, Email `wawanpointer+{runId}-112@qwertysystem.net`) dan Non-Login User `Konversi Lima Pointer {runId}-112` dengan Represented By `Wawan Pointer {runId}-112` yang sudah di-Convert menjadi Login User (Tabel Data Uji Pre-setup No. 10 dan 11).
- Pembanding hanya dibaca: Login User `Ahmad Fauzi` dan Non-Login User `Budi Kurniawan` (Represented By `Ahmad Fauzi`) pada Pre-setup No. 10 dan 11.
- Baseline (S-12): pada langkah awal dicatat jumlah entri Activity Log dan System Log aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit`; sebelum tiap aksi dicatat nilai Last Update dan jumlah entri Tab Changelog Detail record terkait. Kemampuan membaca jumlah entri disediakan tim FE/BE.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-112` yang tersisa (termasuk Login User hasil Convert).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` (dirujuk sebagai `Fixture.nonLoginUser.<key>`) untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

1. Buka Global Settings > Activity Log lewat sidebar dan catat jumlah entri aktor Siti Nurhaliza untuk object Non-Login User per Action `Edit` sebagai baseline Activity Log
2. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User) dan catat jumlah entri per Action `Edit` sebagai baseline System Log aktor

### TC-GS-NLU-182: Edit tanpa perubahan menampilkan toast netral dan tidak menulis log

3. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Edit Nol {runId}-112`, tekan Enter, klik Name baris tersebut, klik tab `Changelog`, dan catat jumlah entri sebagai baseline Changelog `Edit Nol`
4. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Edit Nol {runId}-112`, tekan Enter, dan catat nilai kolom Last Update baris tersebut sebagai baseline Last Update
5. Klik `⋯` baris `Edit Nol {runId}-112` > `Edit`
6. Klik `[Save]` tanpa mengubah field apa pun
7. Verifikasi toast netral (Info, tanpa prefix): `No changes to save.`
8. Verifikasi popup Edit Non-Login User tertutup normal
9. Klik Name baris `Edit Nol {runId}-112` untuk membuka Detail, lalu klik tab `Changelog`
10. Verifikasi kolom header tabel Tab Changelog Detail tampil
11. Verifikasi Tab Changelog Detail: jumlah entri sama dengan baseline (tidak ada entri log baru)
12. Buka Global Settings > Activity Log lewat sidebar
13. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` sama dengan baseline
14. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
15. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` sama dengan baseline
16. Buka sub-tab Non-Login User lewat sidebar, lalu ketik Search `Edit Nol {runId}-112`, tekan Enter
17. Verifikasi nilai kolom Last Update baris `Edit Nol {runId}-112` sama dengan baseline Last Update

### TC-GS-NLU-183: Edit Employee ID yang hanya berbeda huruf besar kecil dianggap tanpa perubahan

18. Ketik Search `Edit Besar {runId}-112`, tekan Enter, klik Name baris tersebut, klik tab `Changelog`, dan catat jumlah entri sebagai baseline Changelog `Edit Besar`
19. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Edit Besar {runId}-112`, tekan Enter, klik `⋯` baris `Edit Besar {runId}-112` > `Edit`
20. Ubah Employee ID dari `EDT-{runId}-0112` menjadi `edt-{runId}-0112` (huruf kecil seluruhnya; `{runId}` berhuruf kecil sehingga hanya huruf besar kecil yang berbeda)
21. Klik `[Save]`
22. Verifikasi toast netral: `No changes to save.`
23. Klik Name baris `Edit Besar {runId}-112` untuk membuka Detail
24. Verifikasi Employee ID pada General Information tetap `EDT-{runId}-0112`
25. Klik tab `Changelog`
26. Verifikasi Tab Changelog Detail: jumlah entri sama dengan baseline (tidak ada entri log baru)
27. Buka Global Settings > Activity Log lewat sidebar
28. Verifikasi Activity Log: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` sama dengan baseline
29. Buka tab `System Log` pada Detail aktor Siti Nurhaliza (Global Settings > User > User List > Login User)
30. Verifikasi System Log aktor: jumlah entri aktor Siti Nurhaliza untuk object Non-Login User dengan Action `Edit` sama dengan baseline

### TC-GS-NLU-425: Import User Non Login tidak menulis entri Create per baris di thread Changelog Non-Login User

31. Buka sub-tab Non-Login User lewat sidebar, ketik Search `Impor Dua {runId}-112`, tekan Enter, klik Name baris tersebut, lalu klik tab `Changelog`
32. Verifikasi empty state Tab Changelog Detail `Impor Dua`: `No changelog yet`
33. Verifikasi empty state Tab Changelog Detail `Impor Dua`: `Activities and changes will appear here.`
34. Verifikasi Tab Changelog Detail `Impor Dua`: tidak ada entri `Create` untuk `Impor Dua {runId}-112` di thread Non-Login User
35. Buka sub-tab Non-Login User lewat sidebar, klik icon `Changelog` pada Table Tools, lalu ketik Search `Impor Dua {runId}-112`, tekan Enter
36. Verifikasi Modal Changelog agregat: empty state `No results found` tampil (tidak ada entri `Create` untuk `Impor Dua {runId}-112`)
37. Tutup Modal Changelog dengan `✕`, lalu buka log Import
38. Verifikasi log Import: ringkasan job Import "User Non Login" yang membuat `Impor Dua {runId}-112` tercatat

### TC-GS-NLU-469: Delete Login User mengosongkan pointer record hasil Convert tanpa entri log

39. Buka Global Settings > User > User List > sub-tab Login User, ketik Search `Konversi Lima Pointer {runId}-112`, tekan Enter, klik Name baris tersebut, klik tab `Changelog`, dan catat jumlah entri sebagai baseline Changelog `Konversi Lima Pointer`
40. Buka sub-tab Login User, ketik Search `Wawan Pointer {runId}-112`, tekan Enter, klik `⋯` baris `Wawan Pointer {runId}-112` > `Delete`
41. Klik `[Delete]` pada dialog konfirmasi
42. Tunggu aksi selesai (dialog Delete menutup)
43. Ketik Search `Konversi Lima Pointer {runId}-112`, tekan Enter, klik Name baris tersebut untuk membuka Detail Login User, lalu klik tab `Changelog`
44. Verifikasi kolom header tabel Tab Changelog Detail `Konversi Lima Pointer` tampil
45. Verifikasi Tab Changelog Detail `Konversi Lima Pointer`: jumlah entri sama dengan baseline, tidak ada entri baru `Edit` Field `Represented By`
46. Buka sub-tab Login User, ketik Search `Ahmad Fauzi`, tekan Enter, klik Name baris `Ahmad Fauzi` untuk membuka Detail, lalu klik tab `Non-Login User`
47. Verifikasi tab `Non-Login User` Ahmad Fauzi: baris pembanding `Budi Kurniawan` tampil
48. Verifikasi tab `Non-Login User` Ahmad Fauzi: `Konversi Lima Pointer {runId}-112` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 3, 4, 16, 18, 19, 31, 35, 39, 40, 43, dan 46 (membuka sub-tab dan Search record yang dicari, R-16) dan langkah 42 (Tunggu aksi selesai), serta navigasi sidebar dan klik Name di blok baca-log.
- Spec absence (kelas g, bagian 3 prinsip 13g): tiap TC memakai record dan baseline sendiri (S-12). Anchor positif absence (bagian 8b butir 2): toast netral `No changes to save.` untuk TC-GS-NLU-182 dan 183; empty state Tab Changelog Detail `No changelog yet` dan `Activities and changes will appear here.` (record hasil Import tidak punya entri Changelog) serta empty state `No results found` hasil Search untuk TC-GS-NLU-425; header kolom Tab Changelog Detail dan baris pembanding `Budi Kurniawan` untuk TC-GS-NLU-469.
- Di atas 35 langkah, alasan: Langkah baca-log berpola dan baseline tidak dihitung menurut Smell bagian 3 prinsip 13: nominal 48 langkah, 31 langkah blok baca-log, 17 langkah terhitung.
- TC-GS-NLU-182 dan 183 mengasersi toast netral; TC-GS-NLU-395 sampai 397 (presence) ada di spec 108.
- Login User pada TC-GS-NLU-469 adalah `Wawan Pointer {runId}-112` milik spec, bukan Login User Pre-setup `Wawan Setiadi`, supaya Delete tidak mengubah data bersama (S-06).
- Temuan untuk QA:
  - TC-GS-NLU-425 Expected a: record hasil Import tidak memiliki entri Changelog (cf. TC-GS-NLU-335 dan 483), sehingga Tab Changelog Detail `Impor Dua` menampilkan empty state; spec memakai empty state itu sebagai anchor positif, bukan header kolom tabel.
  - TC-GS-NLU-182 dan 183 menyebut "Changelog, Activity Log, maupun System Log aktor" tanpa jalur navigasi surface itu; spec memakai Tab Changelog Detail record, Global Settings > Activity Log, dan tab `System Log` pada Detail aktor dengan baseline jumlah entri per Action dan aktor.
  - TC-GS-NLU-182 Expected b menyebut "Last Update tidak berubah" tanpa menyebut langkah mengamatinya; spec mencatat nilai Last Update sebelum aksi dan membandingkannya setelah aksi.
  - TC-GS-NLU-425 Expected b (ringkasan job tercatat di log Import) tidak menyebut lokasi log Import; langkah "buka log Import" ditulis tanpa jalur dan perlu dilengkapi QA. Mekanisme membuat `Impor Dua` lewat Import pada hook `before` juga tidak disebut TC.
  - TC-GS-NLU-469 Expected b menyebut "tab Non-Login User milik Login User mana pun" sedangkan langkah TC hanya membuka Detail Ahmad Fauzi; spec mengasersi tab Ahmad Fauzi saja (S-02).
  - TC-GS-NLU-469 menghapus Login User Pre-setup `Wawan Setiadi` yang juga dipakai TC-GS-NLU-415; spec memakai Login User milik spec.
