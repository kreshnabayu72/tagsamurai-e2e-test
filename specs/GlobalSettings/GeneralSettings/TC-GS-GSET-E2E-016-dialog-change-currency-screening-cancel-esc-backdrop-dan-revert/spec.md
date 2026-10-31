---
id: TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert
title: "Dialog Change Currency: Screening, Backdrop, Esc, Cancel, dan Revert Tanpa Menyimpan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-37
  - TC-GS-GSET-115
  - TC-GS-GSET-40
  - TC-GS-GSET-39
  - TC-GS-GSET-42
coverage:
  web: automated
---

# Dialog Change Currency: Screening, Backdrop, Esc, Cancel, dan Revert Tanpa Menyimpan

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi).
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > General Settings (dibuka hook `beforeEach` suite).
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Record General Settings Client A pada awal spec: baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`), dipulihkan hook `beforeEach` suite lewat PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`). Spec ini tidak pernah menyimpan perubahan, sehingga record tidak berubah.
- Kemampuan teknis:
  - `Spectra.intercept()` sebagai penghitung request PUT `/v2/enterprise-management/general-settings` yang tetap meneruskan request ke server; dipasang di langkah 1 dan dilepas di langkah 35. Dipakai untuk asersi "tidak ada request simpan".
  - Memuat ulang halaman dengan konfirmasi bawaan browser `beforeunload` dikonfirmasi otomatis oleh harness (langkah 28: form dalam keadaan belum tersimpan), tanpa langkah bersyarat.
  - Menekan `Tab` berulang kali dan membaca elemen yang berfokus (fokus terjebak di dalam dialog).
- Data Uji: Currency Code `USD`. Teks Title dan Body dialog dari TC-GS-GSET-37 (PRD §4.2a). Tidak ada Data Dinamis dan tidak ada baris Changelog yang dihasilkan.
- TC-GS-GSET-37, 115, 40, 39, 42: login sebagai Total Control dan berada di Global Settings > General Settings.

## Test Steps

### TC-GS-GSET-37: Screening Dialog Change Currency

1. Pasang penghitung request PUT general settings (intercept, request diteruskan ke server)
2. Pilih Currency Code `USD`
3. Klik `[Save]`
4. Verifikasi Dialog Change Currency muncul
5. Verifikasi penghitung request PUT bernilai 0 (dialog muncul sebelum request simpan terkirim)
6. Verifikasi Title dialog: `Change Currency`
7. Verifikasi Body dialog: `Amounts already entered elsewhere in the app (e.g. Purchase Price) will not be converted — they'll simply be displayed under the new currency symbol. For example, an amount saved as 7,000 will still show as 7,000 — just with the new symbol. No conversion is applied. Are you sure you want to change the currency?`
8. Verifikasi Footer dialog: `[Cancel]` (text, contrast) dan `[Change Currency]` (primary)

### TC-GS-GSET-115: Klik backdrop tidak menutup dialog

9. Klik area backdrop di luar dialog
10. Verifikasi Dialog Change Currency tetap terbuka
11. Verifikasi penghitung request PUT tetap bernilai 0

### TC-GS-GSET-40: Esc setara Cancel

12. Tekan `Tab` berulang kali
13. Verifikasi fokus keyboard terjebak di dalam dialog (tidak keluar dari dialog selama terbuka)
14. Tekan `Esc`
15. Verifikasi dialog tertutup (setara `[Cancel]`)
16. Verifikasi penghitung request PUT tetap bernilai 0
17. Verifikasi tidak ada toast
18. Verifikasi Currency Code tetap `USD`
19. Verifikasi form tetap unsaved: Button "Save" enabled

### TC-GS-GSET-39: Klik Cancel menutup dialog tanpa menyimpan

20. Klik `[Save]`
21. Verifikasi Dialog Change Currency muncul
22. Klik `[Cancel]`
23. Verifikasi dialog tertutup
24. Verifikasi penghitung request PUT tetap bernilai 0
25. Verifikasi tidak ada toast
26. Verifikasi Currency Code tetap `USD` (tidak reset ke nilai lama)
27. Verifikasi form tetap unsaved: Button "Save" enabled
28. Muat ulang halaman (F5), konfirmasi bawaan browser `beforeunload` dikonfirmasi
29. Verifikasi Currency Code kembali `IDR` (tidak tersimpan)

### TC-GS-GSET-42: Currency Code dikembalikan ke nilai tersimpan

30. Pilih Currency Code `USD`
31. Pilih kembali Currency Code `IDR`
32. Verifikasi Button "Save" disabled
33. Verifikasi tidak ada dialog
34. Verifikasi penghitung request PUT tetap bernilai 0 (tidak ada request)
35. Lepas penghitung request PUT

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. Mode: FE+BE. Spec fungsional (satu topik: Dialog Change Currency tanpa menyimpan).
- Urutan TC di spec berbeda dari urutan sumber: 37, 115, 40, 39, 42. TC-GS-GSET-115 dan TC-GS-GSET-40 melanjutkan dialog yang masih terbuka dari TC-GS-GSET-37: keadaannya sama dengan precondition TC tersebut (Currency Code `USD` terpilih, `[Save]` sudah diklik), sehingga langkah 1 sampai 2 TC-GS-GSET-115 dan TC-GS-GSET-40 tidak diulang. TC-GS-GSET-39 mengklik `[Save]` lagi pada form yang sama (langkah 20) dan TC-GS-GSET-42 dimulai dari form bersih sesudah muat ulang (langkah 28).
- Pemetaan Expected: TC-GS-GSET-37 a ke langkah 4 dan 5, b ke 6, c ke 7, d ke 8; TC-GS-GSET-115 ke langkah 10 dan 11; TC-GS-GSET-40 ke langkah 13, 15 sampai 19; TC-GS-GSET-39 a ke langkah 23 dan 24, b ke 25, c ke 26 dan 27, d ke 29; TC-GS-GSET-42 ke langkah 32 sampai 34.
- Langkah 12 (menekan `Tab`) adalah pemicu pengamatan fokus terjebak (TC-GS-GSET-40); fokus diasersi sebelum `Esc` menutup dialog (bagian 8b butir 5).
- Langkah 35 melepas intercept penghitung (penghubung); langkah 21 (Verifikasi dialog muncul) menjadi anchor positif sebelum asersi absence request pada langkah 24.
- Temuan untuk QA:
  - TC-GS-GSET-39: langkah 4 TC (spec langkah 28) memuat ulang halaman saat form masih berisi perubahan belum tersimpan (`USD`), sehingga browser menampilkan konfirmasi bawaan `beforeunload` (PC §24.1d). TC tidak menyebut konfirmasi itu; spec mengonfirmasinya otomatis (Prerequisites).
  - TC-GS-GSET-37: Expected a ("tidak ada request PUT") membutuhkan cara menghitung request; spec memakai penghitung intercept.
  - TC-GS-GSET-42: Expected "tidak ada request" tidak punya padanan UI selain Button "Save" disabled; spec memakai penghitung intercept yang sama.
