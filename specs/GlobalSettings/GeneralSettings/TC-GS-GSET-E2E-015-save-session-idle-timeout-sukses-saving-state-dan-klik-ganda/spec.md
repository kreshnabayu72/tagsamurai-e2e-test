---
id: TC-GS-GSET-E2E-015-save-session-idle-timeout-sukses-saving-state-dan-klik-ganda
title: "Save Session Idle Timeout: Sukses, State Saving, dan Klik Ganda pada Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-28
  - TC-GS-GSET-36
  - TC-GS-GSET-44
  - TC-GS-GSET-45
coverage:
  web: automated
---

# Save Session Idle Timeout: Sukses, State Saving, dan Klik Ganda pada Save

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`).
- Kemampuan teknis:
  - Klien HTTP dengan sesi API Total Control Client A (`Spectra.env.GS_TC_PASSWORD`) untuk PUT `/v2/enterprise-management/general-settings` dengan payload baseline `currencyCode` `IDR`, `timezone` `Asia/Jakarta`, `dateFormat` `dd/MM/yy`, `timeFormat` `HH:mm`, `sessionIdleTimeout` `30`, untuk memulihkan baseline di antara blok (langkah 9 dan 20).
  - `Spectra.intercept()` pada PUT `/v2/enterprise-management/general-settings`: (a) menahan respons selama 5 detik sebelum diteruskan ke server (data uji TC-GS-GSET-44, bukan aturan PRD; menahan respons hanya untuk mengamati state Saving, bukan kelas b); (b) penghitung jumlah request PUT yang tetap meneruskan request ke server (TC-GS-GSET-45). Kedua intercept dilepas segera setelah dipakai (langkah 19 dan 33).
- Data Uji: Session Idle Timeout `1 hour`. Tidak ada Data Dinamis yang dibuat; baris Changelog dihasilkan oleh Save spec ini dan tidak dihapus (audit trail permanen).
- Baseline Changelog: jumlah baris Modal Changelog hasil Search `Session Idle Timeout` dicatat sebelum aksi TC-GS-GSET-45 (langkah 21 sampai 23) dan dipakai pada asersi langkah 32 (S-12).
- Spec mengubah record Client A sehingga suite berjalan serial (`parallel: false`, lihat `suite.md`); hook `after` suite memulihkan baseline.
- TC-GS-GSET-28, 36, 44, 45: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-28 dan TC-GS-GSET-36: Save Session Idle Timeout sampai sukses

1. Pilih Session Idle Timeout `1 hour`
2. Klik `[Save]`
3. Verifikasi tidak ada dialog tambahan sebelum request simpan (Dialog Change Currency dan Dialog Unsaved Changes tidak tampil)
4. Verifikasi toast sukses: `Success, general settings has been saved.`
5. Verifikasi Button "Save" kembali disabled (form di-rebase ke nilai tersimpan)
6. Muat ulang halaman (F5)
7. Verifikasi Session Idle Timeout `1 hour`
8. Verifikasi field lain tidak berubah: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`
9. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), lalu muat ulang halaman (F5)

### TC-GS-GSET-44: State Saving membekukan seluruh kontrol form

10. Tahan respons PUT general settings selama 5 detik (intercept, request diteruskan ke server)
11. Pilih Session Idle Timeout `1 hour`
12. Klik `[Save]`
13. Verifikasi Button "Save" menampilkan loading state
14. Coba ubah Select "Date Format" selama menunggu (buka Select, pilih `M/d/yy`)
15. Verifikasi kelima Select (Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout) dibekukan (disabled)
16. Verifikasi Date Format tetap `dd/MM/yy` (tidak dapat diubah)
17. Tunggu respons PUT diterima (penahanan 5 detik selesai)
18. Verifikasi toast sukses: `Success, general settings has been saved.`
19. Lepas intercept penahanan respons
20. Pulihkan record ke baseline lewat PUT API (lihat Prerequisites), lalu muat ulang halaman (F5)

### TC-GS-GSET-45: Klik ganda cepat pada Save hanya diproses sekali

21. Buka Modal Changelog lewat ikon Changelog di header halaman, ketik Search `Session Idle Timeout`, tekan Enter
22. Catat jumlah total baris hasil Search sebagai `{nIdle}` (0 bila hasil kosong)
23. Tutup Modal Changelog lewat `✕`
24. Tunggu toast lama (langkah 18) hilang otomatis
25. Pasang penghitung request PUT general settings (intercept, request diteruskan ke server)
26. Pilih Session Idle Timeout `1 hour`
27. Klik ganda cepat `[Save]`
28. Verifikasi Button "Save" disabled dan loading setelah klik pertama
29. Verifikasi penghitung mencatat tepat 1 request simpan
30. Verifikasi tepat 1 toast sukses: `Success, general settings has been saved.`
31. Buka Modal Changelog, ketik Search `Session Idle Timeout`, tekan Enter
32. Verifikasi jumlah total baris hasil Search sama dengan `{nIdle}` + 1 (tepat 1 baris baru untuk field Session Idle Timeout)
33. Tutup Modal Changelog lewat `✕`, lalu lepas penghitung request

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Spec fungsional (Save Session Idle Timeout); penahanan respons pada TC-GS-GSET-44 hanya untuk mengamati state Saving.
- TC-GS-GSET-28 dilebur ke blok TC-GS-GSET-36 (langkah 1 sampai 9): keduanya Save Session Idle Timeout `30 minutes` ke `1 hour` lalu F5, tanpa alur baru. Pemetaan Expected: TC-GS-GSET-28 a ke langkah 4, b ke langkah 7; TC-GS-GSET-36 a ke langkah 3, b ke 4, c ke 5, d ke 7 dan 8.
- Pemetaan Expected TC-GS-GSET-44: a ke langkah 13, b ke 15 dan 16, c ke 18. Pemetaan Expected TC-GS-GSET-45: a ke langkah 28 dan 29, b ke 30, c ke 32.
- Langkah penghubung: langkah 9 dan 20 (memulihkan baseline lewat API dan memuat ulang halaman); langkah 17 (menunggu penahanan respons selesai); langkah 19 dan 33 (melepas intercept); langkah 21 sampai 23 dan 31 (membaca baseline dan baris Changelog Search `Session Idle Timeout`); langkah 24 (menunggu toast lama hilang sebelum menghitung toast).
- Jumlah baris Changelog tidak diasersi sebagai angka absolut (S-12): hanya selisih terhadap `{nIdle}`.
- Langkah 14 mencoba mengubah Date Format pada Select yang dibekukan; hasil percobaan diasersi pada langkah 15 dan 16 sebelum respons dilepas (langkah 17), supaya state Saving diasersi tepat waktu.
- Temuan untuk QA:
  - TC-GS-GSET-36: Post Condition a (Changelog dan Activity Log mencatat perubahan) dan b (event `general_settings.updated`) tidak punya langkah observasi di TC-GS-GSET-36 dan TC-GS-GSET-28, sehingga tidak diasersi. Baris Changelog hanya diasersi lewat Expected c TC-GS-GSET-45.
  - TC-GS-GSET-45: "1 request" diukur lewat penghitung intercept pada PUT; TC tidak menyebut cara menghitung request.
