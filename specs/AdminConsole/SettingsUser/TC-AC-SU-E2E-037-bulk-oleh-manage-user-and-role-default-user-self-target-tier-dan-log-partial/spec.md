---
id: TC-AC-SU-E2E-037-bulk-oleh-manage-user-and-role-default-user-self-target-tier-dan-log-partial
title: "Bulk oleh Manage user and role (Update): Default User dan Self Dikecualikan, Target Total Control atau Read Only Skipped, dan Log Partial"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-113
  - TC-AC-SU-125
  - TC-AC-SU-576
  - TC-AC-SU-651
coverage:
  web: automated
---

# Bulk oleh Manage user and role (Update): Default User dan Self Dikecualikan, Target Total Control atau Read Only Skipped, dan Log Partial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user and role Update (U=true, Pre-setup #4) `manageUserRoleUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_MUR_UPDATE_PASSWORD`.
- Env var `AC_MUR_UPDATE_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan pemilik repo (nama ditetapkan penulis spec). Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini sebagai Manage user and role (Update, U=true); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis tambahan: pengamatan request jaringan yang keluar dari browser (ada atau tidaknya request ke server) disediakan tim FE; endpoint tidak dikarang di spec (S-13).
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-125, 576, 651 | `Dewi Lestari` | `Dewi Lestari {runId}-037` | `dewilestari+{runId}-037@qwertysystem.net` | Total Control, Active |
| TC-AC-SU-125 | `John Doe` | `John Doe {runId}-037` | `johndoe+{runId}-037@qwertysystem.net` | Activated, Active |
| TC-AC-SU-125 | `Rina Putri` | `Rina Putri {runId}-037` | `rinaputri+{runId}-037@qwertysystem.net` | Activated, Active |
| TC-AC-SU-576 | `Jane Smith` | `Jane Smith {runId}-037` | `janesmith+{runId}-037@qwertysystem.net` | Activated, Active, tanpa tingkat akses (menjadi Inactive sesudah TC-AC-SU-576) |
| TC-AC-SU-651 | `Jane Smith` | `Jane Smith T651 {runId}-037` | `janesmitht651+{runId}-037@qwertysystem.net` | Activated, Inactive, tanpa tingkat akses (dari seeding, tidak diubah spec) |

- TC-AC-SU-113 memakai Search atas substring bersama `_automated_{namaCompany}` yang menampilkan akun aktor Pre-setup di entitas Principal: Default User (Pre-setup #1), baris aktor sendiri (Pre-setup #4), dan akun lain (Pre-setup #2, #3, #5, #6); tidak ada data dinamis untuk blok itu dan data Pre-setup tidak diubah. N dari seeding: N = 4 (jumlah akun aktor selain Default User dan self) untuk Search itu.
- Changelog modul diverifikasi lewat Popup Changelog: User; entri baru dicari lewat Search atas nama bersuffix (baseline nol, S-12). Kemampuan Search di popup Changelog diasumsikan tersedia seperti tab log lain (lihat Temuan untuk QA).
- Seeding di hook `before` (termasuk `Jane Smith T651 {runId}-037` berstatus Inactive untuk blok TC-AC-SU-651), penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-113: Baris Default User dan self dikecualikan dari seleksi dan hitungan Select All

1. Ketik Search `_automated_{namaCompany}`, tekan Enter
2. Hover checkbox baris Default User
3. Verifikasi checkbox Default User visible namun disabled dengan tooltip `Default User cannot be modified.`
4. Hover checkbox baris aktor sendiri
5. Verifikasi checkbox self visible namun disabled dengan tooltip `You can't manage your own account from here.`
6. Centang 1 baris selain Default User dan baris aktor sendiri
7. Klik `[Select All (4 records)]`
8. Verifikasi `[N]` = 4 tidak menghitung baris Default User dan baris aktor sendiri
9. Verifikasi baris Default User tetap unchecked
10. Verifikasi baris aktor sendiri tetap unchecked
11. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-125: Bulk Deactivate oleh Manage user and role, target Total Control masuk kelompok skipped

12. Ganti isi kotak search dengan `{runId}-037`, tekan Enter
13. Centang `Dewi Lestari {runId}-037`, `John Doe {runId}-037`, dan `Rina Putri {runId}-037`
14. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
15. Verifikasi dialog dua kelompok: kelompok deactivated berisi `John Doe {runId}-037` dan `Rina Putri {runId}-037`; kelompok skipped berisi `Dewi Lestari {runId}-037`
16. Klik `[Continue]`
17. Verifikasi toast sukses: "Success, user has been deactivated. Some items were skipped."

### TC-AC-SU-576: Bulk Deactivate partial hanya menulis entri untuk user yang berhasil

18. Centang `Jane Smith {runId}-037` dan `Dewi Lestari {runId}-037`
19. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`, amati dialog dua kelompok
20. Klik `[Continue]`
21. Verifikasi toast `Success, user has been deactivated. Some items were skipped.`
22. Klik icon Changelog di toolbar
23. Verifikasi `Settings > User > Popup Changelog: User` terbuka
24. Ketik Search `Jane Smith {runId}-037` pada popup Changelog, tekan Enter
25. Verifikasi Changelog memuat tepat 1 baris Deactivate untuk `Jane Smith {runId}-037`
26. Ganti isi kotak search popup Changelog dengan `Dewi Lestari {runId}-037`, tekan Enter
27. Verifikasi empty state `No results found` (tidak ada baris untuk `Dewi Lestari {runId}-037`)
28. Tutup popup Changelog dengan `✕`

### TC-AC-SU-651: Bulk Deactivate tanpa baris eligible, dialog blok, seleksi dipertahankan

29. Centang `Dewi Lestari {runId}-037` dan `Jane Smith T651 {runId}-037`
30. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
31. Verifikasi dialog blok Title `Cannot Deactivate Users` dengan `[×]`
32. Verifikasi body `None of the selected users can be deactivated (already inactive, inactive in Global Settings, or no permission):` dengan bullet `Dewi Lestari {runId}-037` dan bullet `Jane Smith T651 {runId}-037`
33. Verifikasi tombol tunggal `[OK]`
34. Verifikasi tidak ada dialog konfirmasi `Deactivate Users`
35. Verifikasi tidak ada tombol `[Continue]`
36. Verifikasi tidak ada request ke server
37. Verifikasi tidak ada toast
38. Klik `[OK]`
39. Verifikasi dialog tertutup
40. Verifikasi Bulk Action Bar tetap tampil `2 Users selected`
41. Batalkan centang `Jane Smith T651 {runId}-037` (seleksi tersisa `Dewi Lestari {runId}-037`)
42. Klik `[Bulk Action ▾]` lalu pilih `Deactivate`
43. Verifikasi dialog blok Title `Cannot Deactivate User` (singular)
44. Verifikasi body `This user cannot be deactivated (already inactive, inactive in Global Settings, or no permission):` dengan bullet `Dewi Lestari {runId}-037`
45. Verifikasi tombol `[OK]`
46. Klik `[OK]`, lalu klik icon `×` pada bulk action bar untuk membatalkan seleksi
47. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 dan 12 (Search untuk membatasi baris, R-16), langkah 6 (centang satu baris agar Bulk Action Bar dan `[Select All]` muncul; anchor positif tambahan bagi Verifikasi langkah 8 sampai 10, dasar 8b.2), langkah 11 dan 46 (batalkan seleksi sebelum TC berikutnya, S-09), langkah 24 (Search di popup Changelog untuk menemukan entri milik spec, bukan asersi, R-16), langkah 28 (tutup popup), langkah 47 (reset Search).
- Urutan TC dalam spec (S-05 dan S-10): 113 (tanpa mengubah status), 125 dan 576 (Continue mengubah status), 651 (memakai `Jane Smith T651 {runId}-037` yang di-seed Inactive dan `Dewi Lestari` yang tetap Active karena selalu skipped).
- Alasan memuat empat TC (aktor Manage user and role sama, permukaan bulk yang sama): empat blok pada satu halaman dan satu akun; tiap blok berdiri sendiri dengan data seed yang tidak diubah blok lain.
- Ukuran spec (47 langkah, di atas smell sekitar 35 langkah): satu akun dan satu permukaan (Bulk Action Bar) dengan dua dialog bulk yang masing-masing diasersi per klausa (S-01); tidak dipecah lebih lanjut.
- Temuan untuk QA:
  - TC-AC-SU-576 langkah 3 membuka Popup Changelog: User tanpa langkah Search; spec menambahkan Search atas nama bersuffix agar entri milik spec dapat ditemukan dan dihitung (baseline nol, S-12); kemampuan Search di popup Changelog User tidak dinyatakan eksplisit untuk popup ini di TC.
  - TC-AC-SU-576 butir c ("tidak ada baris untuk Dewi Lestari") adalah asersi absence dalam TC yang sama dengan presence; anchor positifnya adalah baris Deactivate `Jane Smith {runId}-037` dan empty state `No results found` pada Search atas nama `Dewi Lestari {runId}-037`.
  - TC-AC-SU-113 memakai nama aktor "Manage user and role (Update)" tanpa nama; spec memakai akun Pre-setup #4. Nilai `[N]` = 4 diturunkan dari jumlah akun aktor Pre-setup (#2, #3, #5, #6) selain Default User dan self; bila ada akun lain yang cocok dengan Search itu, nilai N berbeda.
  - TC-AC-SU-651 Post Condition (switch tetap ON; tidak ada entri log) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Nama user TC (`Dewi Lestari`, `John Doe`, `Rina Putri`, `Jane Smith`) dipakai sebagai nama bersuffix `{runId}-037` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
