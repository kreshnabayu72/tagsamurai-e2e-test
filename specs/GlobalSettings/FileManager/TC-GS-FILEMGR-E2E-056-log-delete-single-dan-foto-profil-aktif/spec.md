---
id: TC-GS-FILEMGR-E2E-056-log-delete-single-dan-foto-profil-aktif
title: "Pencatatan Log Delete Single: Tiga Surface, Entri Photo pada Changelog User, dan File Bukan Foto Aktif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-225
  - TC-GS-FILEMGR-226
  - TC-GS-FILEMGR-227
coverage:
  web: automated
---

# Pencatatan Log Delete Single: Tiga Surface, Entri Photo pada Changelog User, dan File Bukan Foto Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`). Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Data milik spec (suffix `{runId}-056`, seeding lewat fixture BE di hook `before`; mekanisme seeding tidak didefinisikan di TC, disediakan tim FE/BE):
  - User milik spec `Maya Wijaya {runId}-056`, `Alexander Graham Bell {runId}-056`, dan `Fajar Nugroho {runId}-056` (klon pemilik file Tabel A2/D05; user Pre-setup bersama tidak diubah, S-06).
  - `maya-wijaya-{runId}-056.jpg` (salinan F07), file aktif milik `Maya Wijaya {runId}-056`, dipakai TC-225.
  - `alex-photo-{runId}-056.jpeg` (salinan F03), foto profil aktif `Alexander Graham Bell {runId}-056`, dipakai TC-226.
  - `inactive-photo-01-{runId}-056.jpg` (salinan D05), file aktif milik `Fajar Nugroho {runId}-056` yang bukan foto profil aktif (`is_referenced = false`), dipakai TC-227.
- Baseline log: nama file bersuffix unik, sehingga jumlah entri awal di Changelog File Manager, System Log, dan Activity Log adalah nol untuk nama itu. Baseline jumlah baris Changelog User `Fajar Nugroho {runId}-056` dicatat pada langkah 1 sebelum aksi.
- Dependensi TC (TC-64 Delete single, TC-61 Delete file bukan foto aktif) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus permanen lewat API file bersuffix `{runId}-056` yang masih ada dan hapus user milik spec.
- Tidak ada state global yang diubah.

## Test Steps

### Persiapan baseline

1. Buka Global Settings > User > Detail User `Fajar Nugroho {runId}-056`, buka modal Changelog User, catat jumlah baris sebagai baseline TC-227, tutup modal, lalu buka Global Settings > File Manager

### TC-GS-FILEMGR-225: Log Delete single di tiga surface

2. Ketik Search `maya-wijaya-{runId}-056`, tekan Enter
3. Klik ikon (⋯) baris `maya-wijaya-{runId}-056.jpg`, klik `Delete`, lalu klik [Delete]
4. Tunggu aksi selesai
5. Klik ikon Changelog di toolbar, ketik Search `maya-wijaya-{runId}-056`, tekan Enter
6. Verifikasi Changelog File Manager: tepat satu baris Action `Delete`, File Name `maya-wijaya-{runId}-056.jpg`, Field `File Name`, Old Value `maya-wijaya-{runId}-056.jpg`, New Value `—`, Modified By `Sinta M`
7. Tutup modal Changelog lewat `✕`, buka Global Settings > User > Detail User Sinta Maharani > tab System Log, ketik Search `maya-wijaya-{runId}-056`, tekan Enter
8. Verifikasi System Log Detail User Sinta Maharani: tepat satu baris Action `Delete`, Object `File Manager`, Name `maya-wijaya-{runId}-056.jpg`, Field `File Name`, Old Value `maya-wijaya-{runId}-056.jpg`, New Value `—`
9. Buka Global Settings > Activity Log, ketik Search `maya-wijaya-{runId}-056`, tekan Enter
10. Verifikasi Activity Log: tepat satu baris Action `Delete`, Object `File Manager`, Name `maya-wijaya-{runId}-056.jpg`, Field `File Name`, Old Value `maya-wijaya-{runId}-056.jpg`, New Value `—`, Modified By `Sinta M`
11. Buka Global Settings > File Manager

### TC-GS-FILEMGR-227: Delete file yang bukan foto profil aktif hanya soft-delete

12. Ketik Search `inactive-photo-01-{runId}-056`, tekan Enter
13. Klik ikon (⋯) baris `inactive-photo-01-{runId}-056.jpg`, klik `Delete`, lalu klik [Delete]
14. Verifikasi toast sukses: "Success, inactive-photo-01-{runId}-056.jpg has been deleted."
15. Klik tombol Recycle Bin di toolbar, ketik Search `inactive-photo-01-{runId}-056`, tekan Enter
16. Verifikasi `inactive-photo-01-{runId}-056.jpg` tampil di Recycle Bin dengan Deleted By `Sinta M`
17. Tutup modal Recycle Bin lewat `✕`, klik ikon Changelog di toolbar, ketik Search `inactive-photo-01-{runId}-056`, tekan Enter
18. Verifikasi Changelog File Manager: tepat satu baris Action `Delete` untuk `inactive-photo-01-{runId}-056.jpg`
19. Tutup modal Changelog lewat `✕`, buka Global Settings > User > Detail User `Fajar Nugroho {runId}-056`, buka modal Changelog User
20. Verifikasi jumlah baris Changelog User `Fajar Nugroho {runId}-056` sama dengan baseline langkah 1
21. Verifikasi Changelog User `Fajar Nugroho {runId}-056` tidak memuat baris Field `Photo` baru
22. Tutup modal Changelog User, lalu buka Global Settings > File Manager

### TC-GS-FILEMGR-226: Delete foto profil aktif menghasilkan entri Photo di tiga surface

23. Ketik Search `alex-photo-{runId}-056`, tekan Enter
24. Klik ikon (⋯) baris `alex-photo-{runId}-056.jpeg`, klik `Delete`, lalu klik [Delete]
25. Tunggu aksi selesai
26. Buka Global Settings > User > Detail User `Alexander Graham Bell {runId}-056`, buka modal Changelog User
27. Verifikasi Changelog User: tepat satu baris Action `Edit`, Field `Photo`, Old Value `alex-photo-{runId}-056.jpeg`, New Value `—`, Modified By `Sinta M`
28. Tutup modal, buka Global Settings > User > Detail User Sinta Maharani > tab System Log, ketik Search `alex-photo-{runId}-056`, tekan Enter
29. Verifikasi System Log Detail User Sinta Maharani: tepat satu baris Action `Edit`, Object `User`, Name `Alexander Graham Bell {runId}-056`, Field `Photo`, Old Value `alex-photo-{runId}-056.jpeg`, New Value `—`
30. Buka Global Settings > Activity Log, ketik Search `alex-photo-{runId}-056`, tekan Enter
31. Verifikasi Activity Log: tepat satu baris Action `Edit`, Object `User`, Name `Alexander Graham Bell {runId}-056`, Field `Photo`, Old Value `alex-photo-{runId}-056.jpeg`, New Value `—`, Modified By `Sinta M`

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Kelas pencatatan (log tiga surface).
- Urutan TC di spec berbeda dari sumber (225, 227, 226): ketiganya menghapus file milik spec dan tidak saling membutuhkan; urutan 227 sebelum 226 tidak berdampak karena data terpisah. Baseline Changelog User Fajar dicatat di awal (langkah 1), sebelum aksi pemicu pertama.
- Nama Pre-setup literal pada TC (`maya-wijaya.jpg`, `alex-photo.jpeg`, `inactive-photo-01.jpg`, user `Alexander Graham Bell`) diganti salinan bersuffix milik spec karena aksi Delete atas Pre-setup bersama dilarang (S-06) dan "tepat satu baris" butuh nama unik (S-12). Nilai `Name` pada log mengikuti nama user klon bersuffix.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline), langkah 4 dan 25 (Tunggu aksi selesai sebelum pindah surface), langkah 2, 12, 23 (Search nama bersuffix pada tabel utama), langkah 7, 17, 19, 22, 28 (menutup modal dan pindah halaman), langkah 11 (kembali ke File Manager), langkah 15 (Search pada Recycle Bin).
- Asersi tidak ada baris Photo baru pada Changelog User Fajar (langkah 21) memakai baseline jumlah baris (langkah 1 dan 20) sebagai anchor; ini asersi jumlah/state, bukan kelas g (keputusan D-1 opsi B, tidak ada spec absence terpisah).
- Temuan untuk QA:
  - Mekanisme seeding file, user pemilik, dan flag `is_referenced` tidak didefinisikan di TC (Q-4, NC-15); ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-227 langkah 4 "Changelog User" tidak menyebut surface log lain untuk butir d; hanya Changelog User yang diasersi.
  - TC-225, 226 tidak menyebut toast sukses; spec tidak mengasersinya.
