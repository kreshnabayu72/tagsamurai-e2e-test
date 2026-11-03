---
id: TC-FA-SU-E2E-032-resilience-status-aktif-single-server-error-5xx-pemeriksaan-gagal-dan-kegagalan
title: "Resilience Status Aktif Single: Server Error 5xx, Pemeriksaan Gagal, dan Kegagalan Penulisan Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-95
  - TC-FA-SU-101
  - TC-FA-SU-102
  - TC-FA-SU-103
coverage:
  web: automated
---

# Resilience Status Aktif Single: Server Error 5xx, Pemeriksaan Gagal, dan Kegagalan Penulisan Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20) dan layanan terkendali (#37: layanan pemeriksaan aset dan approval serta penulisan log dapat di-intercept atau dikendalikan penguji). Target memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE):
  - `Gita Permata {runId}-032-A`, email `gita.permata+{runId}-032-a@qwertysystem.net`: Active (TC-FA-SU-101).
  - `Doni Prasetyo {runId}-032`, email `doni.prasetyo+{runId}-032@qwertysystem.net`: Inactive (TC-FA-SU-102).
  - `Gita Permata {runId}-032-B`, email `gita.permata+{runId}-032-b@qwertysystem.net`: Active, tanpa aset aktif (TC-FA-SU-95).
  - `Gita Permata {runId}-032-C`, email `gita.permata+{runId}-032-c@qwertysystem.net`: Active (TC-FA-SU-103).
- Kemampuan teknis:
  - `Spectra.intercept()` atas respons HTTP di atas backend nyata: request Deactivate dan Activate dibuat 5xx; request pemeriksaan aset aktif dan approval tertunda (layanan Borrow, Assignment, Approvals) dibuat timeout. Tiap intercept dilepas segera setelah pemicunya (S-09).
  - Pemicu kegagalan penulisan log di sisi server untuk TC-FA-SU-103 disediakan tim FE/BE (TC menyatakan kegagalan hanya dapat dipicu di sisi server); dipulihkan ke normal di langkah terakhir dan di hook `after`.
  - Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): hook `before` mencatat baseline jumlah entri pengguna milik spec pada Tab Changelog target serta total entri Tab System Log aktor dan Activity Log; asersi berupa jumlah sama dengan baseline.
  - Kemampuan baca state BE status aktif pengguna (disediakan tim FE/BE).
- State global: kegagalan penulisan log (TC-FA-SU-103) dipulihkan di hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-101: Deactivate gagal karena server error 5xx

1. Ketik Search `Gita Permata {runId}-032-A`, tekan Enter
2. Pasang intercept: respons request Deactivate menjadi 5xx
3. Klik sakelar Active pada baris `Gita Permata {runId}-032-A`
4. Klik `[Deactivate]`
5. Verifikasi toast error "Error, failed to deactivate user." tampil
6. Lepas intercept request Deactivate
7. Verifikasi sakelar Active baris `Gita Permata {runId}-032-A` kembali ke ON
8. Verifikasi data pengguna utuh: status aktif `Gita Permata {runId}-032-A` tetap Active menurut server
9. Verifikasi jumlah entri Tab Changelog `Gita Permata {runId}-032-A`, total entri Tab System Log aktor, dan total entri Activity Log sama dengan baseline

### TC-FA-SU-102: Activate gagal karena server error 5xx

10. Tunggu toast lama hilang otomatis
11. Ganti isi kotak search dengan `Doni Prasetyo {runId}-032`, tekan Enter
12. Pasang intercept: respons request Activate menjadi 5xx
13. Klik sakelar Active pada baris `Doni Prasetyo {runId}-032`
14. Klik `[Activate]`
15. Verifikasi toast error "Error, failed to activate user." tampil
16. Lepas intercept request Activate
17. Verifikasi sakelar Active baris `Doni Prasetyo {runId}-032` kembali ke OFF
18. Verifikasi jumlah entri Tab Changelog `Doni Prasetyo {runId}-032`, total entri Tab System Log aktor, dan total entri Activity Log sama dengan baseline

### TC-FA-SU-95: Pemeriksaan aset dan approval gagal atau timeout

19. Ganti isi kotak search dengan `Gita Permata {runId}-032-B`, tekan Enter
20. Pasang intercept: respons pemeriksaan aset aktif dan approval tertunda menjadi timeout
21. Klik sakelar Active pada baris `Gita Permata {runId}-032-B`
22. Verifikasi dialog `Deactivate User` tetap tampil (tidak diblokir) dengan baris `We couldn't check this user's active assets or pending approvals. You can still continue.`
23. Verifikasi baris peringatan pemeriksaan gagal tampil sebelum pertanyaan penutup
24. Lepas intercept pemeriksaan aset aktif dan approval tertunda
25. Verifikasi tombol `[Deactivate]` Enabled
26. Klik `[Deactivate]`
27. Verifikasi sakelar Active baris `Gita Permata {runId}-032-B` berpindah ke OFF

### TC-FA-SU-103: Penulisan log Deactivate gagal tidak membatalkan Deactivate

28. Ganti isi kotak search dengan `Gita Permata {runId}-032-C`, tekan Enter
29. Picu kegagalan penulisan log di sisi server
30. Klik sakelar Active pada baris `Gita Permata {runId}-032-C`
31. Klik `[Deactivate]`
32. Verifikasi toast "Success, user has been deactivated." tampil
33. Buka Detail `Gita Permata {runId}-032-C` > Tab Changelog, muat ulang
34. Verifikasi header Detail menampilkan status aktif Inactive (tidak di-rollback)
35. Verifikasi Tab Changelog tidak memuat entri `Deactivate` untuk pengguna ini
36. Pulihkan penulisan log ke kondisi normal

## Notes

- Alasan sekitar 35 langkah (36): semua blok satu kelas harness (kegagalan yang dipaksakan, kelas b) dan berdiri sendiri dengan pengguna milik spec sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 11, 19, dan 28 (mengganti isi kotak search yang masih berisi nama sebelumnya, bagian 8b butir 9), langkah 10 (menunggu toast error sebelumnya hilang sebelum toast berikutnya, R-12), langkah 6, 16, dan 24 (melepas intercept, S-09), dan langkah 36 (memulihkan kegagalan penulisan log).
- Klausa "tanpa log" TC-FA-SU-101 dan TC-FA-SU-102 diasersi sebagai jumlah terhadap baseline (bukan spec absence); anchor-nya baseline yang dicatat hook `before`.
- Pembagian TC lintas spec: TC-FA-SU-107, TC-FA-SU-118, TC-FA-SU-119, dan TC-FA-SU-134 (resilience bulk) ada di spec 033.
- Temuan untuk QA:
  - TC-FA-SU-101 Expected butir b menyebut "data utuh" tanpa menyatakan data apa; spec menafsirkannya sebagai status aktif tetap Active menurut server (langkah 8).
  - TC-FA-SU-103 Expected butir b bersyarat ("bila tetap gagal"). Spec mengasumsikan kegagalan penulisan log dipertahankan sepanjang langkah 29 sampai 35; percobaan ulang penulisan log tidak teramati dari UI sehingga tidak diasersi. Post Condition butir b diasersi pada langkah 35 karena langkah 3 TC me-refresh Tab Changelog; toast sukses pada langkah 32 menjadi anchor.
  - Teks toast sukses Deactivate pada TC-FA-SU-103 ("toast sukses tampil") dikutip dari TC-FA-SU-87.
  - TC-FA-SU-103 berautomation `Manual Only BE` dan tidak menyebut cara memicu kegagalan penulisan log; dicatat sebagai kemampuan "disediakan tim FE/BE".
  - Post Condition TC-FA-SU-95 butir b (Auth) tidak punya langkah observasi dan tidak diasersi; butir a diasersi pada langkah 27.
  - Target TC (Gita Permata, Doni Prasetyo) adalah pengguna Pre-setup bersama; spec memakai pengguna milik spec dengan suffix (S-06).
