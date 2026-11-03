---
id: TC-FA-FAAM-E2E-007-propagasi-perubahan-sesi-lain-ke-list-dan-modal
title: "Propagasi Perubahan Sesi Lain: List Auto-Refresh dan Modal Terbuka Tidak Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-37
  - TC-FA-FAAM-38
  - TC-FA-FAAM-643
coverage:
  web: automated
---

# Propagasi Perubahan Sesi Lain: List Auto-Refresh dan Modal Terbuka Tidak Berubah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Sesi B (pelaku kedua): sesi API aktor Total Control yang sama, token tidak dihitung sebagai sesi web (lihat `suite.md`; kemampuan disediakan tim BE/FE). Sesi B hanya memicu perubahan data dan bukan konteks UI kedua; sesi UI A adalah satu-satunya yang diasersi.
- Data Dinamis (suffix `{runId}-007`, seed dan cleanup di hook `before` dan `after`):
  - `Ergonomic Chair {runId}-007`: salinan seed API fixture `Ergonomic Chair` (#11) ber-Code unik per run, dipakai TC-FA-FAAM-38 sebagai target Edit tanpa Save; UoM awal `Pcs`.
  - `Realtime Item {runId}-007`: dibuat sesi B pada langkah 3 (TC-FA-FAAM-37), dihapus hook `after`.
  - `Concurrent Item {runId}-007`: dibuat sesi B pada langkah 23 (TC-FA-FAAM-643), dihapus hook `after`.
  - `Partial Item {runId}-007`: nilai yang diketik di Modal Create sesi A, tidak disimpan.
  - Data master yang dibutuhkan sesi B untuk membuat Asset Name (Category leaf `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`) dari Pre-setup #22 s.d. #24.
- Jendela SSE 5 detik: pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya; dipakai pada langkah 14 dan 24 sebelum asersi absence propagasi.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-37: List auto-refresh diam-diam saat sesi lain membuat Asset Name

1. Ketik Search `Realtime Item {runId}-007`, tekan Enter di sesi A
2. Amati List sesi A dan biarkan terbuka
3. Sesi B membuat Asset Name `Realtime Item {runId}-007` hingga tersimpan
4. Amati List sesi A tanpa memuat ulang halaman
5. Verifikasi baris `Realtime Item {runId}-007` muncul di List sesi A
6. Verifikasi tidak ada dialog di sesi A
7. Verifikasi halaman aktif sesi A tidak berubah (tetap halaman 1)
8. Verifikasi Search sesi A tidak berubah (kotak Search masih berisi `Realtime Item {runId}-007`)
9. Verifikasi Sort sesi A tidak berubah (header Asset Name masih menampilkan indikator sort default)

### TC-FA-FAAM-38: Modal Edit yang sedang terbuka tidak di-refresh oleh perubahan sesi lain

10. Ganti isi kotak search dengan `Ergonomic Chair {runId}-007`, tekan Enter
11. Klik `⋯` baris `Ergonomic Chair {runId}-007` lalu `Edit`
12. Ubah Code menjadi `CHR-09` tanpa Save
13. Sesi B mengubah UoM `Ergonomic Chair {runId}-007` menjadi `Set` hingga tersimpan
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Verifikasi Modal Edit sesi A tetap terbuka dengan Code `CHR-09` yang diketik
16. Verifikasi tidak ada dialog interupsi di sesi A
17. Klik `✕` pada Modal Edit
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`

### TC-FA-FAAM-643: Modal Create terbuka tidak berubah oleh perubahan data sesi lain

20. Ganti isi kotak search dengan `Concurrent Item {runId}-007`, tekan Enter
21. Klik `[+ Asset Name]`
22. Isi sebagian Modal Create dengan Asset Name `Partial Item {runId}-007`
23. Sesi B membuat Asset Name `Concurrent Item {runId}-007` hingga tersimpan
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Verifikasi Modal Create sesi A tetap terbuka dengan input `Partial Item {runId}-007` dipertahankan
26. Verifikasi List di balik modal ter-refresh diam-diam dengan baris `Concurrent Item {runId}-007` tampil
27. Klik `✕` pada Modal Create
28. Verifikasi dialog `Unsaved Changes` tampil
29. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 37, 38, 643 (urutan sumber; TC-643 membuka form terakhir dan menutupnya dengan `[Leave]`, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 10, 20 (Search untuk menemukan atau menyiapkan baris target, R-16; langkah 1 dan 20 juga menetapkan state Search sesi A supaya baris baru dari sesi B tampil di halaman 1), langkah 2 dan 4 (mengamati List), langkah 14 dan 24 (jendela SSE 5 detik, bagian 6), langkah 17 dan 19, serta 27 dan 29 (menutup form dirty dengan `✕` dan `[Leave]`, S-08/S-09; `Verifikasi` dialog `Unsaved Changes` pada langkah 18 dan 28 diwajibkan S-08).
- Sesi B memakai sesi API (pelaku kedua yang hanya memicu perubahan state), sehingga tidak memakai `P-2` (keputusan 2026-10-30). Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah 6 dan 16 (absence dialog) memakai baris yang muncul pada langkah 5 dan Modal Edit yang tetap terbuka pada langkah 15 sebagai anchor positif; langkah 14 memberi jendela SSE sebelum asersi absence.
- Temuan untuk QA:
  - TC-37, TC-38, dan TC-643 menulis "sesi A" dan "sesi B" sebagai dua sesi UI paralel (Automation `Manual Only — (d) dua sesi paralel`); spec memakai sesi B lewat sesi API karena sesi B hanya memicu perubahan.
  - TC-38 memakai `Ergonomic Chair` (Pre-setup #11) sebagai target ubah UoM sesi B; fixture bersama tidak boleh diubah (S-06), sehingga spec memakai salinan seed API `Ergonomic Chair {runId}-007` (salinan tidak tercantum di Tabel Data Uji Dinamis).
  - TC-37 tidak menyebut keadaan Search, Sort, dan halaman sesi A sebelum sesi B bertindak, padahal Expected "tidak berubah" bergantung padanya; spec menetapkan Search `Realtime Item {runId}-007` (hasil kosong), Sort default, dan halaman 1 (S-14).
  - TC-643 b ("List di balik modal ter-refresh") tidak menyebut cara mengamati list yang tertutup modal; spec mengasersi baris baru pada List di balik modal lewat Search yang ditetapkan sebelum modal dibuka.
