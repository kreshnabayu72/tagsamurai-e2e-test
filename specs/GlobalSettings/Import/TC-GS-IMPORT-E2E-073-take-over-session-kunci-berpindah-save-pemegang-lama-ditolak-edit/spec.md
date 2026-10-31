---
id: TC-GS-IMPORT-E2E-073-take-over-session-kunci-berpindah-save-pemegang-lama-ditolak-edit
title: "Take Over Session: Kunci Berpindah, Save Pemegang Lama Ditolak (Edit Session Taken Over), dan Cancel pada Dialog Tidak Mengubah Kunci"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-868@L1077
  - TC-GS-IMPORT-870@L1079
coverage:
  web: automated
---

# Take Over Session: Kunci Berpindah, Save Pemegang Lama Ditolak (Edit Session Taken Over), dan Cancel pada Dialog Tidak Mengubah Kunci

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Dua sesi browser (kelas multi-konteks), konteks terpisah dengan sesi login sendiri, keduanya login di hook `before` dan berada di Import > Brand Client A:
  - Sesi TC: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`.
  - Sesi Admin kedua: Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks Sesi Admin kedua dan mengembalikan sesi ke akun default suite.
- Data Dinamis (Client A, dipulihkan lewat skrip fixture sebelum tiap TC): D-01 draft Brand 12 baris `pending` dari `brand-12.csv` (Row # 1 `Acme Corp`, #2 `Lenovo`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk kedua sesi. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft D-01 dipulihkan antar TC; sesi edit yang masih terbuka ditutup lewat `[Cancel]`.

## Test Steps

### TC-GS-IMPORT-870 (baris L1079): Cancel pada dialog Konflik Kunci Sesi tidak mengubah kunci

1. [Sesi TC] Klik `⋯` pada baris #1
2. [Sesi TC] Pilih Edit
3. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
4. [Sesi Admin kedua] Klik `⋯` pada baris #2
5. [Sesi Admin kedua] Pilih Edit
6. [Sesi Admin kedua] Verifikasi dialog Konflik Kunci Sesi dengan tombol `[Cancel]` dan `[Take Over Session]`
7. [Sesi Admin kedua] Klik `[Cancel]`
8. [Sesi Admin kedua] Verifikasi baris #2 tidak menjadi input
9. [Sesi Admin kedua] Verifikasi footer Admin kedua tetap `[Import (12)]`
10. [Sesi TC] Klik `[Save]`
11. [Sesi TC] Verifikasi toast "Success, row has been updated."
12. [Sesi TC] Verifikasi baris #1 menampilkan `Acme Corporation` berstatus `pending`
13. Pulihkan draft D-01
14. [Sesi TC] Muat ulang halaman Import > Brand
15. [Sesi Admin kedua] Muat ulang halaman Import > Brand

### TC-GS-IMPORT-868 (baris L1077): Take Over Session

16. [Sesi TC] Klik `⋯` pada baris #1
17. [Sesi TC] Pilih Edit
18. [Sesi TC] Ubah Brand Name baris #1 menjadi `Acme Corporation`
19. [Sesi Admin kedua] Klik `⋯` pada baris #2
20. [Sesi Admin kedua] Pilih Edit
21. [Sesi Admin kedua] Verifikasi dialog Title "Draft Is Being Edited" dengan Body "Another admin is currently editing this draft. Taking over ends their edit session, and their unsaved changes will not be saved." dan tombol `[Cancel]` dan `[Take Over Session]`
22. [Sesi Admin kedua] Klik `[Take Over Session]`
23. [Sesi Admin kedua] Verifikasi dialog tertutup
24. [Sesi Admin kedua] Verifikasi sesi edit belum terbuka untuk Admin kedua
25. [Sesi Admin kedua] Klik `⋯` pada baris #2
26. [Sesi Admin kedua] Pilih Edit
27. [Sesi Admin kedua] Verifikasi baris #2 menjadi input aktif
28. [Sesi Admin kedua] Verifikasi footer menampilkan `[Cancel]` dan `[Save]`
29. [Sesi TC] Klik `[Save]`
30. [Sesi TC] Verifikasi dialog Title "Edit Session Taken Over" dengan Body "Another admin took over this edit session. Your unsaved changes were not saved." dan tombol `[OK]` saja
31. [Sesi TC] Klik `[OK]` pada dialog
32. [Sesi TC] Muat ulang halaman Import > Brand
33. [Sesi TC] Verifikasi baris #1 menampilkan `Acme Corp` (perubahan Total Control tidak tersimpan)
34. [Sesi Admin kedua] Klik `[Cancel]` pada footer; pulihkan draft D-01

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: multi-konteks (kelas c, prinsip 13c); kedua sesi UI menjadi objek asersi.
- Urutan TC dibalik terhadap nomor TC: blok TC-GS-IMPORT-870@L1079 lebih dulu karena tidak mengubah kunci; TC-GS-IMPORT-868@L1077 memindahkan kunci sehingga di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 dan 34 (pemulihan draft dan penutupan sesi edit), langkah 14 dan 15 (muat ulang halaman kedua sesi sesudah draft dipulihkan), langkah 32 (muat ulang).
- Pembagian TC lintas spec: nomor TC-GS-IMPORT-868, 869, 870, dan 871 masing-masing dipakai dua baris dengan isi berbeda. Spec ini memuat 868@L1077 dan 870@L1079; 868@L738 ada di spec 049, 871@L1080 di spec 072, dan 869@L1078 di spec 077.
- Temuan untuk QA:
  - ID ganda TC-GS-IMPORT-868 (L738 dan L1077), 869 (L937 dan L1078), 870 (L1020 dan L1079), 871 (L938 dan L1080) dengan isi berbeda; `sourceTc` dan `check-suite.py` tidak dapat membedakannya. Usulan: QA memberi nomor baru pada empat baris di L1077-L1080.
  - TC-GS-IMPORT-870@L1079 Expected a hanya menyebut "dialog Konflik Kunci Sesi" tanpa teks Title dan Body; spec memakai nama dialog dari TC.
