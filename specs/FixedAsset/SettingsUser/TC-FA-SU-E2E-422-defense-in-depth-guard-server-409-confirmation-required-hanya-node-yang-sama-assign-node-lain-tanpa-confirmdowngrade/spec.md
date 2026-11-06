---
id: TC-FA-SU-E2E-422-defense-in-depth-guard-server-409-confirmation-required-hanya-node-yang-sama-assign-node-lain-tanpa-confirmdowngrade
title: "Defense-in-depth Guard Server 409 confirmation_required Hanya untuk Turun Tangga pada Node yang Sama, Assign di Node Lain Tanpa confirmDowngrade"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1109
coverage:
  web: automated
---

# Defense-in-depth Guard Server 409 confirmation_required Hanya untuk Turun Tangga pada Node yang Sama, Assign di Node Lain Tanpa confirmDowngrade

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21: Finance & Accounting dengan anak Accounts Payable), dan Transaction Role (#39). Target: Mira Anggraini, Disposal × Staff pada Finance & Accounting dan Borrowing & Assignment × Approver pada Finance & Accounting.
- Data uji: penugasan Disposal × Monitoring & Report pada Accounts Payable (node lain), lalu pada Finance & Accounting (node sama), masing-masing tanpa `confirmDowngrade`, kemudian dengan `confirmDowngrade = true`.
- Nilai nama pengguna, grup, dan penugasan dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor (Total Control Lina Marlina) untuk permintaan langsung assign Transaction Role dengan dan tanpa flag `confirmDowngrade`; pembacaan state penugasan Transaction Role Mira Anggraini lewat fixture BE; pembacaan entri Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log lewat kemampuan baca BE. Entri log muncul eventual: pembacaan diulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global dan pemulihan: penugasan Transaction Role Mira Anggraini berubah oleh langkah 1 dan 9 (Staff pada Finance & Accounting diganti Monitoring & Report), beserta Last Updated dan entri log. Dipulihkan ke Pre-setup #39 lewat seed API pada langkah 15 dan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1109: Guard server: 409 confirmation_required hanya untuk turun tangga pada node yang sama; assign di node lain tidak membutuhkan confirmDowngrade

1. Kirim permintaan langsung ke API assign Disposal × Monitoring & Report pada Accounts Payable untuk Mira Anggraini (Staff hanya pada Finance & Accounting) tanpa `confirmDowngrade` memakai klien HTTP dengan token sesi Lina Marlina
2. Verifikasi permintaan langkah 1 diterima (sukses) tanpa flag karena Accounts Payable bukan node penugasan Staff
3. Verifikasi penugasan baru Disposal × Monitoring & Report pada Accounts Payable tersimpan (dibaca lewat API)
4. Verifikasi Staff pada Finance & Accounting tidak berubah (dibaca lewat API)
5. Tunggu entri log langkah 1 tersimpan lalu catat jumlah entri yang menyebut Accounts Payable pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sebagai baseline
6. Kirim permintaan langsung assign Disposal × Monitoring & Report pada Finance & Accounting untuk Mira Anggraini tanpa `confirmDowngrade` memakai klien HTTP dengan token sesi Lina Marlina
7. Verifikasi permintaan langkah 6 ditolak dengan status 409 `confirmation_required` karena turun tangga pada node yang sama tanpa flag
8. Verifikasi seluruh Save dibatalkan tanpa perubahan: Staff pada Finance & Accounting tetap ada, penugasan Monitoring & Report pada Finance & Accounting tidak ada, dan penugasan Accounts Payable dari langkah 1 tidak berubah (dibaca lewat API)
9. Kirim ulang permintaan langkah 6 dengan `confirmDowngrade = true` memakai klien HTTP dengan token sesi Lina Marlina
10. Verifikasi permintaan langkah 9 diterima
11. Verifikasi Staff pada Finance & Accounting diganti Monitoring & Report (Staff tidak ada dan Monitoring & Report ada pada Disposal × Finance & Accounting, dibaca lewat API)
12. Tunggu entri log langkah 9 tersimpan hingga pasangan entri tampil pada Tab Changelog Mira Anggraini
13. Verifikasi Tab Changelog Mira Anggraini memuat pasangan entri `Remove` (Staff) lalu `Assign` (Monitoring & Report) pada Finance & Accounting
14. Verifikasi jumlah entri yang menyebut Accounts Payable pada Tab Changelog Mira Anggraini, Tab System Log aktor, dan Activity Log sama dengan baseline langkah 5 (tidak ada entri per descendant)
15. Pulihkan Mira Anggraini ke Pre-setup #39 lewat seed API

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- K-1 dan bagian 8b butir 1: TC-FA-SU-1109 bertipe Security dengan kolom FE Test kosong (`-`) dan Expected berupa respons API (status respons dan state data). TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint, mengikuti spec 335; asersi spec hanya status respons dan state data (dibaca lewat API dan kemampuan baca BE), bukan tampilan UI. TC-FA-SU-1003 (permintaan serupa tanpa penanda konfirmasi, 409 dan 422) ada di spec 335.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, S-03): langkah 5 dan 12 (menunggu entri log eventual, baseline dicatat per S-12), dan langkah 15 (pemulihan, S-09). Pengiriman permintaan langsung (langkah 1, 6, 9) adalah pemicu, bukan asersi.
- Pembacaan "tabel dan log" pada Langkah Uji 4 TC memakai pembacaan state penugasan lewat fixture BE (langkah 3, 4, 8, 11) dan kemampuan baca BE untuk entri log (langkah 13, 14), sesuai 8b butir 1; tampilan Sub-tab Transaction Role tidak diasersi di spec ini.
- Anchor 8b butir 2: langkah 14 (jumlah entri Accounts Payable sama dengan baseline) didahului langkah 13 (pasangan entri `Remove` dan `Assign` untuk langkah 9 tampil pada surface yang sama).
- Temuan untuk QA:
  - Konfirmasi: TC-FA-SU-1109 bertipe Security dengan kolom FE Test kosong namun tidak tercatat hanya-BE; spec ditulis FE+BE dengan klien HTTP bertoken sesi aktor mengikuti spec 335 (persetujuan pemilik proses). Mohon dikonfirmasi bila seharusnya dicatat hanya-BE.
  - TC-FA-SU-1109 dan TC-FA-SU-1003 mengandalkan flag `confirmDowngrade` dan status 409 `confirmation_required` (FASU-LOGIC-10i); nama flag, nama status, dan perilaku guard perlu dikonfirmasi dengan implementasi BE.
  - Expected d ("tidak ada entri per descendant pada log mana pun") tidak menyebut surface log dan cara mengukurnya; spec membaca tiga surface (Tab Changelog Mira Anggraini, Tab System Log aktor, Activity Log) dan membandingkan jumlah entri yang menyebut Accounts Payable (satu-satunya descendant Finance & Accounting) terhadap baseline langkah 5. Surface dan cara baca perlu dikonfirmasi.
  - Langkah Uji 4 ("Periksa tabel dan log") tidak menyebut cara pemeriksaan tabel; spec membaca state penugasan lewat fixture BE, bukan tampilan Sub-tab Transaction Role. Kemampuan baca hak efektif atau penugasan lewat API disediakan tim BE.
  - TC menyebut "API assign" tanpa nama atau jalur endpoint; spec tidak menulis jalur endpoint (S-13) dan klien HTTP beserta jalur yang dipakai disediakan tim FE/BE.
