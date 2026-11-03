---
id: TC-AC-DN-E2E-187-konkurensi-dua-sesi-ui-last-write-wins
title: "Konkurensi Dua Sesi UI: Edit Record yang Sama, Save Kedua Menimpa Save Pertama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-160
  - TC-AC-DN-571
coverage:
  web: automated
---

# Konkurensi Dua Sesi UI: Edit Record yang Sama, Save Kedua Menimpa Save Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi pertama: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi kedua (konteks browser terpisah, hasilnya diasersi): Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net` (Total Control, entitas Principal; email lewat `Fixture.settings-device-name.akunTotalControl2`), password `Spectra.env.AC_DN_TC2_PASSWORD` (belum terdaftar; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Sesi kedua login dan membuka halaman pada langkah 2 dan 3, dan konteksnya ditutup pada langkah 31.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan #2, Measurement `Unit`, `Meter`, `Box`, node pohon Category `Antenna`. Nama dinamis dibentuk `<nama dasar> {runId}-187` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`, `Meter`, `Box`; #14 Pohon Category (`Antenna`).
- Data Dinamis (milik spec; dibuat lewat API di hook `before`, dihapus di hook `after` termasuk hasil rename; kemampuan seeding disediakan tim FE/BE). Seed tidak menulis entri Changelog.

  | Kode | Nama awal | Measurement | Category | Dipakai oleh |
  |---|---|---|---|---|
  | R1 | `Door Asal {runId}-187` | `Unit` | `Antenna` | TC-AC-DN-160 (sesi pertama menjadi `Door Satu {runId}-187`, sesi kedua `Door Dua {runId}-187`) |
  | R2 | `Kabel Dua Sesi {runId}-187` | `Unit` | `Antenna` | TC-AC-DN-571 (sesi pertama Measurement `Meter`, sesi kedua `Box`) |

- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_TC_PASSWORD` (sudah terdaftar) dan `AC_DN_TC2_PASSWORD`.

## Test Steps

1. Buka konteks browser kedua
2. Di sesi kedua, login sebagai Maya Putri (`Spectra.env.AC_DN_TC2_PASSWORD`)
3. Di sesi kedua, buka halaman `Settings > Device > Device Name`

### TC-AC-DN-160: Dua sesi Edit record yang sama (nama)

4. Di sesi pertama, ketik Search `Door Asal {runId}-187`, tekan Enter
5. Di sesi pertama, buka menu aksi pada baris `Door Asal {runId}-187`, klik `Edit`
6. Di sesi kedua, ketik Search `Door Asal {runId}-187`, tekan Enter
7. Di sesi kedua, buka menu aksi pada baris `Door Asal {runId}-187`, klik `Edit`, ubah nama menjadi "Door Dua {runId}-187", klik `[Save]`
8. Verifikasi toast sukses di sesi kedua
9. Di sesi pertama, kosongkan field Device Name lalu ketik "Door Satu {runId}-187"
10. Di sesi pertama, klik `[Save]`
11. Verifikasi toast sukses "Success, device name has been updated." di sesi pertama
12. Verifikasi popup form sesi pertama tertutup
13. Verifikasi tidak ada dialog konflik dan tidak ada pesan error
14. Verifikasi List sesi pertama memuat baris `Door Satu {runId}-187`
15. Verifikasi List sesi pertama tidak memuat `Door Asal {runId}-187` maupun `Door Dua {runId}-187`
16. Di sesi kedua, muat ulang halaman `Settings > Device > Device Name`
17. Di sesi kedua, ketik Search `Door {runId}-187`, tekan Enter
18. Verifikasi List sesi kedua memuat baris `Door Satu {runId}-187`
19. Verifikasi List sesi kedua tidak memuat `Door Dua {runId}-187`

### TC-AC-DN-571: Dua sesi Edit record yang sama (Measurement)

20. Di sesi pertama, ketik Search `Kabel Dua Sesi {runId}-187`, tekan Enter
21. Di sesi pertama, buka menu aksi pada baris `Kabel Dua Sesi {runId}-187`, klik `Edit`, ubah Measurement menjadi `Meter`
22. Di sesi kedua, ketik Search `Kabel Dua Sesi {runId}-187`, tekan Enter
23. Di sesi kedua, buka menu aksi pada baris `Kabel Dua Sesi {runId}-187`, klik `Edit`, ubah Measurement menjadi `Box`, klik `[Save]`
24. Verifikasi toast sukses "Success, device name has been updated." di sesi kedua
25. Di sesi pertama, klik `[Save]`
26. Verifikasi toast sukses "Success, device name has been updated." di sesi pertama
27. Verifikasi form Edit sesi pertama ditutup
28. Verifikasi tidak ada dialog konflik, tidak ada toast error, dan tidak ada inline error pada form sesi pertama
29. Di sesi pertama, muat ulang halaman, ketik Search `Kabel Dua Sesi {runId}-187`, tekan Enter
30. Verifikasi baris `Kabel Dua Sesi {runId}-187` menampilkan Measurement `Meter`
31. Tutup konteks browser kedua

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Konteks UI kedua dipakai karena hasil di sesi kedua (toast Save, isi List sesudah muat ulang) diasersi (bagian 3 butir P-2: konteks yang diasersi bukan pemicu), sehingga spec ini kelas c dan tidak memakai `P-2`. Pelaku kedua tidak lewat sesi API di spec ini.
- Langkah penghubung (S-03, R-16): langkah 1 sampai 3 menyiapkan sesi kedua (login eksplisit, S-07); langkah 4, 6, 17, 20, 22, 29 (Search) menemukan baris record milik spec; langkah 16 memuat ulang halaman sesi kedua sesuai TC; langkah 31 menutup konteks kedua (S-09). Langkah 17 memakai kata kunci `Door {runId}-187` yang mencakup `Door Satu` dan `Door Dua`.
- Anchor absence (8b butir 2): langkah 14 mendahului langkah 15 dan langkah 18 mendahului langkah 19. Pada langkah 11, TC-AC-DN-160 Expected a menyebut toast sukses di sesi pertama; toast sesi kedua langkah 8 mengikuti langkah TC ("toast sukses tampil") tanpa teks di Expected, sehingga teksnya tidak diasersi.
- Tumpang tindih sumber: TC-AC-DN-160 dan TC-AC-DN-571 sama-sama "Dua sesi Edit record yang sama" (last-write-wins) dengan field berbeda (nama dan Measurement); tiap TC tetap satu spec ini dengan record sendiri.
- Record milik spec (S-06, S-12): R1 dan R2 menggantikan `Door Antenna` dan `Cable Tester` Pre-setup #16 TC sumber; Pre-setup #16 tidak diubah.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-160 (satu entri log Edit per Save sukses di Changelog, Activity Log, dan System Log) dan TC-AC-DN-571 (Measurement tersimpan `Meter`; sudah teramati pada langkah 30 sebagai Expected d).
  - TC-AC-DN-571: sesi kedua menutup form Edit setelah Save sukses (tidak ada dirty); tidak ada pemulihan form.
  - TC memakai nama tanpa suffix; spec memakai nama bersuffix `{runId}-187` (S-12).
