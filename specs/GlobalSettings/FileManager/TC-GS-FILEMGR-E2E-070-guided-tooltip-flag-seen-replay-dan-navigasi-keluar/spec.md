---
id: TC-GS-FILEMGR-E2E-070-guided-tooltip-flag-seen-replay-dan-navigasi-keluar
title: "Guided Tooltip File Manager: Flag Seen, Replay, dan Keluar lewat Navigasi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-35
  - TC-GS-FILEMGR-36
  - TC-GS-FILEMGR-38
coverage:
  web: automated
---

# Guided Tooltip File Manager: Flag Seen, Replay, dan Keluar lewat Navigasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Pengecualian dari hook suite: spec ini menguji flag `guided_tooltip_seen_gs-file-manager` sendiri, sehingga flag direset ke "belum ada" lewat API (hapus flag pada preferensi pengguna aktor; mekanisme disediakan tim FE) pada awal tiap TC yang mensyaratkannya. Hook `before` spec ini mencatat nilai awal flag; hook `after` (tetap jalan walau spec gagal di tengah) memulihkan nilai awal (true dari hook suite).
- Data: Data Pre-setup Tabel A2 di-seed idempotent di hook `before` sehingga tabel utama terisi; spec tidak membuat atau mengubah data.
- Tidak ada state global lain yang diubah.

## Test Steps

### TC-GS-FILEMGR-38: Keluar walkthrough lewat navigasi tidak menetapkan flag seen

1. Hapus flag `guided_tooltip_seen_gs-file-manager` lewat API sehingga flag belum ada
2. Buka Global Settings > File Manager
3. Verifikasi walkthrough muncul otomatis dari Step 1
4. Tanpa klik tombol apa pun pada walkthrough, pindah ke menu Global Settings > Activity Log
5. Verifikasi walkthrough tertutup saat navigasi
6. Buka kembali Global Settings > File Manager
7. Verifikasi walkthrough muncul lagi otomatis dari Step 1 pada kunjungan berikutnya

### TC-GS-FILEMGR-35: Walkthrough muncul otomatis pada kunjungan pertama saja

8. Hapus flag `guided_tooltip_seen_gs-file-manager` lewat API sehingga flag belum ada
9. Muat ulang Global Settings > File Manager
10. Verifikasi walkthrough muncul otomatis dari Step 1 pada kunjungan pertama
11. Klik [Skip] pada Step 1
12. Verifikasi walkthrough tertutup setelah [Skip]
13. Pindah ke menu Global Settings > Activity Log, lalu buka kembali Global Settings > File Manager
14. Verifikasi tabel utama File Manager tampil
15. Verifikasi walkthrough tidak muncul otomatis pada kunjungan berikutnya

### TC-GS-FILEMGR-36: Replay lewat tombol [?] tidak mereset flag seen

16. Muat ulang Global Settings > File Manager
17. Hover tombol [?] di sebelah kanan Breadcrumb
18. Verifikasi tooltip hover tombol [?] menampilkan `Show guide`
19. Klik tombol [?]
20. Verifikasi klik [?] memulai walkthrough dari Step 1
21. Klik [Skip]
22. Muat ulang halaman
23. Verifikasi tabel utama File Manager tampil
24. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang (flag seen tetap)

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas guided tooltip (flag seen, replay, navigasi). Konten Step dan navigasi keyboard ada di spec `TC-GS-FILEMGR-E2E-069-guided-tooltip-konten-navigasi-keyboard` (mock).
- Urutan TC di spec berbeda dari sumber (38, 35, 36): TC-38 meninggalkan flag belum ada, TC-35 menetapkan flag lewat [Skip], dan TC-36 mensyaratkan flag sudah ada (kolom Dependensi TC-36 pada TC-35). Flag direset lewat API pada awal TC-38 dan TC-35 (langkah 1 dan 8) agar precondition "flag belum ada" eksplisit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 8 (reset flag), langkah 9 dan 16 (muat ulang halaman), langkah 13 (pindah menu lalu kembali, TC-35 langkah 3), langkah 14 dan 23 (anchor positif: tabel utama tampil sebelum asersi absence walkthrough sesudah navigasi atau `F5`, bagian 8b butir 2).
- Temuan untuk QA:
  - Mekanisme menghapus flag seen lewat API tidak didefinisikan di TC; ditulis sebagai kemampuan yang disediakan tim FE tanpa mengarang endpoint.
  - TC-35 dan TC-36 tidak memberi cara membaca nilai flag; spec membuktikan flag lewat perilaku walkthrough (tidak muncul otomatis).
