---
id: TC-FA-SU-E2E-428-constraint-berubah-antara-modal-assign-dibuka-dan-submit-ditolak-422-dan-pilihan-stale-dibersihkan
title: "Constraint Berubah antara Modal Assign Dibuka dan Submit: Server Menolak 422, Pilihan Stale Dibersihkan, dan Modal Tetap Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1123
coverage:
  web: automated
---

# Constraint Berubah antara Modal Assign Dibuka dan Submit: Server Menolak 422, Pilihan Stale Dibersihkan, dan Modal Tetap Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi UI A): Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Admin B (Pre-setup #13): pelaku kedua lewat sesi API (login API password, token tidak dihitung sebagai sesi web) yang hanya memicu perubahan state (Edit Home Group); tidak ada sesi UI kedua. Email dan password Admin B tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21). Target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Gita Permata yang dikosongkan lewat seed API di hook `before`, dengan seluruh penugasan Transaction Role Gita Permata berada di Finance & Accounting (precondition TC-FA-SU-1123 Expected a). Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Gita Permata (Home Group dikosongkan pada awal skenario, lalu Finance & Accounting dari Admin B). Gita Permata juga akun aktor Pre-setup #20; di spec ini hanya menjadi pengguna target.
- Data uji: Group IT Infrastructure, Transaction Transfer, Role Monitoring & Report (dipilih pada langkah 4 dan tidak disimpan); Home Group baru Finance & Accounting.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserNoHG` (Pre-setup #50) per target di hook `before`; Admin B mengubah Home Group Gita Permata lewat sesi API; pembacaan Home Group Gita Permata lewat kemampuan baca BE; pencatat request jaringan Spectra (status respons permintaan `[Submit]`). Home Group Gita Permata dipulihkan ke Finance & Accounting lewat seed API di hook `after` sebagai cadangan.
- State global yang diubah: Home Group Gita Permata (dikosongkan di hook `before`, lalu diubah ke Finance & Accounting pada langkah 5); nilai akhir sama dengan Home Group awal Gita Permata (Pre-setup #51) dan dipulihkan lewat seed API di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script (kunci baru: seed #50 per target dan Admin B #13).

## Test Steps

### TC-FA-SU-1123: Constraint berubah antara modal Assign dibuka dan Submit: server menolak 422, pilihan stale dibersihkan, modal tetap terbuka, dan tidak ada perubahan

1. Ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Klik `[+ Assign]`
4. Pilih Group IT Infrastructure, Transaction Transfer, Role Monitoring & Report tanpa klik `[Submit]`
5. Admin B mengubah Home Group Gita Permata ke Finance & Accounting lewat sesi API hingga Home Group tersimpan
6. Verifikasi Edit Home Group Admin B tersimpan tanpa dialog konfirmasi: Home Group Gita Permata = Finance & Accounting lewat kemampuan baca BE
7. Klik `[Submit]`
8. Verifikasi server menolak permintaan `[Submit]` dengan status 422
9. Verifikasi pesan "Gita Permata is no longer eligible. Please select another." tampil
10. Verifikasi pilihan Group IT Infrastructure dibersihkan
11. Verifikasi modal Assign tetap terbuka
12. Klik `[✕]` pada modal
13. Verifikasi dialog `Unsaved Changes`
14. Klik `[Leave]`
15. Verifikasi `[+ Assign]` tampil pada Sub-tab Transaction Role Gita Permata
16. Verifikasi tidak ada baris Transfer × Monitoring & Report pada Sub-tab Transaction Role Gita Permata

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 12, dan 14 (penutupan modal sesuai S-08; `Verifikasi` dialog pada langkah 13 diwajibkan S-08). Search `Gita Permata` pada langkah 1 menemukan baris target (R-16, R-23).
- Admin B memakai sesi API (R-20, langkah 5 ditulis "... hingga ... tersimpan"), bukan konteks UI kedua; butir `P-2` tidak dipakai (keputusan 2026-10-30). Tampilan sesi A tidak di-refresh antara langkah 5 dan 7.
- Expected b TC-FA-SU-1123 dipecah satu `Verifikasi` per klausa: status 422 (langkah 8), pesan copy `V-09` (langkah 9), pilihan dibersihkan (langkah 10), dan modal tetap terbuka (langkah 11). Bentuk tampilan pesan (toast atau inline) belum ditetapkan PRD (NC-27) sehingga langkah 9 tidak mengasersi bentuknya.
- Anchor 8b butir 2: baris Transfer × Monitoring & Report tidak ada (langkah 16) didahului `Verifikasi` `[+ Assign]` tampil pada Sub-tab Transaction Role (langkah 15) sebagai bukti surface termuat.
- Pembagian TC lintas spec (S-05): TC-FA-SU-1123 ada di `sourceTc` spec ini dan spec 432. Spec ini memuat Expected a, Expected b, dan klausa "tidak ada baris Transfer × Monitoring & Report" dari Expected c; klausa "tidak ada entri `Assign` baru" (absence log) hanya di spec 432.
- Temuan untuk QA:
  - TC-FA-SU-1123 berlabel Manual Only (d) dua sesi; spec mengotomasinya dengan Admin B lewat sesi API (R-20) sehingga `coverage.web: automated`. Sesi UI kedua tidak dipakai karena hasil di sesi B tidak diasersi UI.
  - Pre-setup #50 didefinisikan global (Home Group seluruh 25 pengguna dikosongkan); spec memakai penerapan per target (hanya Gita Permata). Konfirmasi bila #50 harus diterapkan penuh.
  - Penugasan Gita Permata pada varian Pre-setup #50 harus seluruhnya berada di Finance & Accounting (Expected a). Pre-setup #51 memuat Damaged × Staff pada IT Infrastructure; bila seed memakai #51, Edit Home Group akan memunculkan dialog D-10 sehingga Expected a tidak berlaku. Seed `FaUserNoHG` untuk Gita Permata mengikuti varian `FaUserMain` (Pre-setup #23).
  - Expected a ("tersimpan tanpa dialog") tidak teramati sebagai dialog karena Admin B memakai sesi API; spec mengasersi Home Group tersimpan lewat kemampuan baca BE (langkah 6).
  - Bentuk tampilan penolakan V-09 (toast atau inline) belum ditetapkan (NC-27); `[User Name]` pada copy V-09 diasumsikan nama pengguna target (Gita Permata).
  - Penutupan modal pada langkah 12 sampai 14 mengikuti S-08 tanpa asersi bersyarat; TC tidak menyebut cara menutup modal setelah penolakan. Modal dianggap dirty karena Transaction dan Role masih terpilih.
  - Seed `FaUserNoHG` (Pre-setup #50) dan Admin B (Pre-setup #13; email dan password tidak tertulis di Pre-setup TC) wajib disediakan tim FE/BE; kunci fixture baru dicatat untuk fixture `fixtures/fixed-asset-settings-user.json`.
  - Post Condition TC-FA-SU-1123 ("Home Group Gita Permata Finance & Accounting dan tidak ada penugasan baru") diasersi hanya sebatas Expected c (langkah 16) dan Home Group (langkah 6).
