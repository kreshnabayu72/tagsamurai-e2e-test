---
id: TC-AC-PP-E2E-005-first-time-create-penutupan-modal
title: "First-time Create Privacy Policy: Penutupan Modal Dirty dan Bersih"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-39
  - TC-AC-PP-40
  - TC-AC-PP-197
  - TC-AC-PP-198
coverage:
  web: automated
---

# First-time Create Privacy Policy: Penutupan Modal Dirty dan Bersih

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE): respons daftar riwayat versi dipaksa 0 versi (Riwayat C). Tidak ada endpoint Publish yang dipanggil.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`. Login nyata di hook `before` hanya untuk run non-mock; pada run mock sesi disediakan harness. Hook `after` mengembalikan sesi ke akun default suite.
- Kebutuhan mock sesi dan izin: payload sesi dan izin Total Control (capability "Manage privacy policy" Read dan Update) agar row action Edit dan [Create Privacy Policy] tampil.
- Dataset Riwayat C (0 versi) lewat mock; tidak ada data yang dibuat.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons daftar riwayat versi 0 versi; kemampuan mengetik, Backspace, Esc, dan klik area gelap di luar modal.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` (dipakai hanya untuk run non-mock).

## Test Steps

### TC-AC-PP-39: Menutup editor first-time yang sudah diketik memunculkan Dialog Unsaved Changes dan Leave tidak menyimpan versi

1. Klik menu Settings > Privacy Policy di sidebar
2. Klik [Create Privacy Policy]
3. Ketik "Unsaved first policy" pada editor
4. Klik `[✕]` di header
5. Verifikasi Dialog "Unsaved Changes" tampil
6. Verifikasi body dialog "You have unsaved changes. Are you sure you want to leave?"
7. Verifikasi tombol dialog `[Cancel]` dan `[Leave]`
8. Klik `[Cancel]`
9. Verifikasi dialog tertutup
10. Verifikasi modal tetap terbuka
11. Verifikasi konten `Unsaved first policy` dipertahankan
12. Klik `[✕]` lagi
13. Klik `[Leave]`
14. Verifikasi modal tertutup sepenuhnya
15. Verifikasi tabel menampilkan empty state first-time

### TC-AC-PP-197: Klik di luar modal Create Privacy Policy yang sudah diketik diabaikan tanpa Dialog Unsaved Changes

16. Klik [Create Privacy Policy]
17. Ketik "Draft first policy" pada editor
18. Klik area gelap di luar modal
19. Verifikasi modal tetap terbuka di state Edit
20. Verifikasi konten `Draft first policy` dipertahankan
21. Verifikasi Dialog Unsaved Changes tidak muncul
22. Klik `[✕]` di header
23. Verifikasi Dialog "Unsaved Changes" tampil
24. Klik `[Leave]`

### TC-AC-PP-198: Konten Create yang diketik lalu dihapus sampai kosong dianggap clean sehingga penutupan tanpa dialog

25. Klik [Create Privacy Policy]
26. Ketik "Temp text" pada editor
27. Tekan Backspace 9 kali sehingga editor kosong kembali
28. Klik `[✕]` di header
29. Verifikasi modal tertutup langsung
30. Verifikasi Dialog Unsaved Changes tidak muncul
31. Verifikasi tabel menampilkan empty state first-time

### TC-AC-PP-40: Menutup editor first-time yang belum diubah lewat [✕] dan Esc langsung tertutup tanpa dialog

32. Klik [Create Privacy Policy]
33. Klik `[✕]` di header
34. Verifikasi modal tertutup langsung (penutupan via `[✕]`)
35. Verifikasi Dialog Unsaved Changes tidak muncul (penutupan via `[✕]`)
36. Verifikasi tabel menampilkan empty state first-time
37. Klik [Create Privacy Policy]
38. Tekan Esc
39. Verifikasi modal tertutup langsung (penutupan via Esc)
40. Verifikasi Dialog Unsaved Changes tidak muncul (penutupan via Esc)
41. Verifikasi tabel menampilkan empty state first-time

## Notes

- Mode: mock. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Semua TC bertanda FE Test "UI Only" di TC sumber.
- Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-05, prinsip 6): TC-AC-PP-40 (penutupan bersih) ditaruh di akhir; TC-AC-PP-197 dan TC-AC-PP-198 mendahuluinya. Setiap kasus memakai form baru (buka form sama dengan jumlah kejadian menutup: lima kali buka, lima kali menutup di langkah 13, 24, 28, 33, 38).
- Langkah penghubung (S-03, S-08): langkah 22–24 menutup form dirty dari TC-AC-PP-197 secara deterministik (`✕`, dialog `Unsaved Changes`, `[Leave]`) agar form berikutnya dapat dibuka; asersi dialog pada langkah 23 ditambahkan sebagai bagian S-08 (bukan Expected TC).
- Temuan untuk QA:
  - TC-AC-PP-197 tidak menyebut cara menutup modal sesudah klik luar diabaikan; spec memakai `✕` lalu `[Leave]` sebagai penutup (S-08).
  - Post Condition "tabel tetap 0 versi" pada keempat TC tidak punya langkah observasi dan tidak diasersi selain empty state yang sudah ada di Expected.
- Ukuran spec (41 langkah, melewati sekitar 35): langkah membengkak karena tiap klausa Expected menjadi satu Verifikasi (S-01) dan tiap kasus membuka form baru (prinsip 6). Satu dataset (Riwayat C), satu akun, tanpa aksi tulis, dan tiap blok TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal; spec tidak dipecah (konvensi bagian 3, batas ukuran).
