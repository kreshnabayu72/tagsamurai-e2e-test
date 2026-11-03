---
id: TC-AC-DN-E2E-159-log-absence-no-op-dan-system-log
title: "Absence Log: Edit Tanpa Perubahan atau Hanya Kapitalisasi Tidak Menulis Entri (Changelog, Activity Log, System Log)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-501
  - TC-AC-DN-502
  - TC-AC-DN-512
coverage:
  web: automated
---

# Absence Log: Edit Tanpa Perubahan atau Hanya Kapitalisasi Tidak Menulis Entri (Changelog, Activity Log, System Log)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19, #20.
- Data Dinamis (milik spec, dibuat lewat API di hook `before`, tanpa SKU): `Pintu Antena {runId}-159`, `Pintu Kapital {runId}-159`, `Pintu Sistem {runId}-159` (semua `Unit`, `Antenna`); tidak berubah oleh aksi. Aksi Edit tanpa perubahan adalah pemicu absence (P-5 butir a).
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah entri Changelog dan Activity Log yang memuat `Pintu Antena {runId}-159` dan `Pintu Kapital {runId}-159`, serta jumlah total entri System Log aktor, sebagai baseline (kemampuan baca)
2. TC-AC-DN-501: Edit tanpa perubahan tidak menulis entri pada Changelog dan Activity Log
3. Ketik Search `Pintu Antena {runId}-159`, tekan Enter
4. Klik ikon row action `⋯` pada baris `Pintu Antena {runId}-159`, lalu klik `Edit`
5. Klik `[Save]` tanpa mengubah field apa pun
6. Verifikasi toast netral "No changes to save."
7. Klik ikon Changelog di toolbar
8. Verifikasi popup `Changelog: Device Name` tampil
9. Ketik Search `Pintu Antena {runId}-159`, tekan Enter
10. Verifikasi jumlah entri Changelog untuk `Pintu Antena {runId}-159` sama dengan baseline (tidak ada baris baru)
11. Klik ikon close `(X)` pada popup Changelog
12. Buka menu `Activity Log`, lalu klik tab `User Action`
13. Verifikasi halaman `Activity Log > User Action` tampil
14. Ketik Search `Pintu Antena {runId}-159`, tekan Enter
15. Verifikasi jumlah entri Activity Log untuk `Pintu Antena {runId}-159` sama dengan baseline (tidak ada entri baru)
16. TC-AC-DN-502: Edit yang hanya mengubah kapitalisasi adalah No-Op
17. Buka halaman `Settings > Device > Device Name`
18. Ketik Search `Pintu Kapital {runId}-159`, tekan Enter
19. Klik ikon row action `⋯` pada baris `Pintu Kapital {runId}-159`, lalu klik `Edit`
20. Ubah field Device Name menjadi "pintu kapital {runId}-159" (hanya kapitalisasi)
21. Klik `[Save]`
22. Verifikasi toast netral "No changes to save." (bukan toast sukses "Success, device name has been updated.")
23. Verifikasi popup form tertutup
24. Verifikasi baris pada List tetap bernama `Pintu Kapital {runId}-159`
25. Klik ikon Changelog di toolbar
26. Verifikasi popup `Changelog: Device Name` tampil
27. Ketik Search `Pintu Kapital {runId}-159`, tekan Enter
28. Verifikasi jumlah entri Changelog untuk `Pintu Kapital {runId}-159` sama dengan baseline
29. Klik ikon close `(X)` pada popup Changelog
30. Buka menu `Activity Log`, lalu klik tab `User Action`
31. Verifikasi halaman `Activity Log > User Action` tampil
32. Ketik Search `Pintu Kapital {runId}-159`, tekan Enter
33. Verifikasi jumlah entri Activity Log untuk `Pintu Kapital {runId}-159` sama dengan baseline
34. TC-AC-DN-512: System Log aktor tidak memuat entri untuk Edit tanpa perubahan
35. Buka halaman `Settings > Device > Device Name`
36. Ketik Search `Pintu Sistem {runId}-159`, tekan Enter
37. Klik ikon row action `⋯` pada baris `Pintu Sistem {runId}-159`, lalu klik `Edit`
38. Klik `[Save]` tanpa mengubah field apa pun
39. Verifikasi toast netral "No changes to save."
40. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
41. Verifikasi halaman `Settings > User > Detail` tampil
42. Klik tab `System Log`
43. Verifikasi tabel System Log aktor tampil
44. Verifikasi total entri System Log aktor sama dengan baseline (tidak ada entri baru untuk Device Name milik spec)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan record spec; baseline dicatat sebelum aksi pertama karena seeding via API dapat menulis entri Create.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (44 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Anchor absence (bagian 8b butir 2): toast netral hasil server (`No changes to save.`) pada TC-AC-DN-501 dan 502; pada TC-AC-DN-512 toast yang sama ditambahkan sebagai anchor.
- Temuan untuk QA:
  - TC-AC-DN-512 tidak menyebut toast netral; spec mengasersinya hanya sebagai anchor absence, mengikuti perilaku TC-AC-DN-501.
  - TC-AC-DN-501 tidak menyebut ukuran baseline; spec memakai jumlah entri sebelum aksi (S-12).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
