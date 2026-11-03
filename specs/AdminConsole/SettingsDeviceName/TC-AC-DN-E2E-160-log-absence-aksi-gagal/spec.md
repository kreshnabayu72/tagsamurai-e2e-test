---
id: TC-AC-DN-E2E-160-log-absence-aksi-gagal
title: "Absence Log: Create, Edit, dan Delete yang Gagal karena Error Server Tidak Menulis Entri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-503
  - TC-AC-DN-504
  - TC-AC-DN-505
coverage:
  web: automated
---

# Absence Log: Create, Edit, dan Delete yang Gagal karena Error Server Tidak Menulis Entri

## Prerequisites

- Mode: FE+BE (intercept).
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19, #20.
- Data Dinamis (milik spec, dibuat lewat API di hook `before`, tanpa SKU, `Unit`, `Antenna`): `Pintu Edit {runId}-160` (TC-AC-DN-504) dan `Pintu Hapus {runId}-160` (TC-AC-DN-505); `Dock Station {runId}-160` tidak pernah tersimpan (TC-AC-DN-503).
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- Kemampuan teknis tambahan (disediakan tim FE/BE): `Spectra.intercept()` di atas backend nyata sebagai pemicu kegagalan server (P-5 butir a); intercept dilepas segera setelah pemicunya selesai (S-09).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah total entri Changelog sebagai baseline T0 (kemampuan baca)
2. TC-AC-DN-503: Create yang gagal karena server error tidak menulis entri
3. Aktifkan intercept yang membuat request Create dijawab server error
4. Klik `+ Device Name`
5. Ketik "Dock Station {runId}-160" pada field Device Name
6. Pilih "Unit" pada field Measurement
7. Pada field Category pilih leaf `Accessory` (expand `TAG` lalu `NFC`)
8. Klik `[Submit]`
9. Verifikasi toast error "Error, failed to create device name."
10. Verifikasi popup form tetap terbuka dengan input dipertahankan
11. Lepas intercept
12. Klik icon close `[✕]`
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Klik ikon Changelog di toolbar
16. Verifikasi popup `Changelog: Device Name` tampil
17. Verifikasi total entri Changelog sama dengan baseline T0 (entri awal tidak bertambah)
18. Ketik Search `Dock Station {runId}-160`, tekan Enter
19. Verifikasi hasil Search `Dock Station {runId}-160` tidak memuat baris baru (empty state `No results found` atau jumlah baris tidak bertambah dari baseline T0)
20. Klik ikon close `(X)` pada popup Changelog
21. TC-AC-DN-504: Edit yang gagal karena server error tidak menulis entri
22. Ketik Search `Pintu Edit {runId}-160`, tekan Enter
23. Klik ikon row action `⋯` pada baris `Pintu Edit {runId}-160`, lalu klik `Edit`
24. Aktifkan intercept yang membuat request Edit dijawab server error
25. Ubah field Device Name menjadi "Pintu Edit Pro {runId}-160"
26. Klik `[Save]`
27. Verifikasi toast error "Error, failed to update device name."
28. Verifikasi popup form tetap terbuka dengan input dipertahankan
29. Lepas intercept
30. Klik icon close `[✕]`
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`
33. Klik ikon Changelog di toolbar
34. Verifikasi popup `Changelog: Device Name` tampil
35. Verifikasi total entri Changelog sama dengan baseline T0 (entri awal tidak bertambah)
36. Ketik Search `Pintu Edit Pro {runId}-160`, tekan Enter
37. Verifikasi hasil Search `Pintu Edit Pro {runId}-160` tidak memuat baris baru (empty state `No results found` atau jumlah baris tidak bertambah dari baseline T0)
38. Klik ikon close `(X)` pada popup Changelog
39. TC-AC-DN-505: Delete yang gagal karena server error tidak menulis entri
40. Ganti isi kotak Search dengan `Pintu Hapus {runId}-160`, tekan Enter
41. Klik ikon row action `⋯` pada baris `Pintu Hapus {runId}-160`, lalu klik `Delete`
42. Aktifkan intercept yang membuat request Delete dijawab server error
43. Klik `[Delete]` pada dialog konfirmasi
44. Verifikasi toast error "Error, failed to delete device name."
45. Verifikasi dialog tetap terbuka
46. Lepas intercept
47. Klik `[Cancel]` pada dialog konfirmasi
48. Klik ikon Changelog di toolbar
49. Verifikasi popup `Changelog: Device Name` tampil
50. Verifikasi total entri Changelog sama dengan baseline T0 (entri awal tidak bertambah)
51. Ketik Search `Pintu Hapus {runId}-160`, tekan Enter
52. Verifikasi hasil Search `Pintu Hapus {runId}-160` tidak memuat baris baru (empty state `No results found` atau jumlah baris tidak bertambah dari baseline T0)
53. Klik ikon close `(X)` pada popup Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): baseline T0 dicatat sebelum aksi pertama; menutup form dirty dengan `✕`, dialog `Unsaved Changes`, dan `[Leave]` (S-08); `[Cancel]` menutup dialog Delete yang tetap terbuka; Search menemukan record spec.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (53 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- P-5 butir a: intercept kegagalan server adalah pemicu absence, bukan objek uji; anchor absence adalah toast error hasil server (bagian 8b butir 2).
- Temuan untuk QA:
  - Ekspektasi 'tetap menampilkan 11 entri awal' memakai angka absolut; spec memakai baseline T0 (S-12).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01): TC-AC-DN-503, 504, 505.
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
