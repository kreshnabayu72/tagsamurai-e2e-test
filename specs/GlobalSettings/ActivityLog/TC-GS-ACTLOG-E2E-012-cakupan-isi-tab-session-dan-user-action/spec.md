---
id: TC-GS-ACTLOG-E2E-012-cakupan-isi-tab-session-dan-user-action
title: "Cakupan Isi Tab Session dan User Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-38
  - TC-GS-ACTLOG-39
  - TC-GS-ACTLOG-40
coverage:
  web: automated
---

# Cakupan Isi Tab Session dan User Action

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun aktor: Total Control Client A (Sari Dewi), `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Activity Log.
- Environment variable: `GS_TC_PASSWORD`, `ACTLOG_PASSWORD` (password uji yang dipasang ke user dinamis modul Activity Log). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor:
  - User `John Doe {runId}-012` (First Name `John`, Last Name `Doe {runId}-012`) dengan akses Fixed Asset, Admin Console, dan Global Settings, email `Fixture.activityLog.johnDoe012.email` (ditetapkan tim FE, fixture baru). Entri yang dibutuhkan dihasilkan oleh aksi nyata user ini secara berurutan pada waktu berbeda: Login platform `Success`, buka card Fixed Asset (`Session started` Fixed Asset), buka card Admin Console (`Session started` Admin Console), lalu buka card Global Settings (`Session started` Global Settings). Password `Spectra.env.ACTLOG_PASSWORD`.
  - User `Rudi Hartono {runId}-012` (First Name `Rudi`, Last Name `Hartono {runId}-012`) yang hanya punya akses Fixed Asset (tanpa akses Global Settings), email `Fixture.activityLog.rudiHartono012.email` (ditetapkan tim FE, fixture baru), dengan satu Login `Success` lewat alur Auth. Password `Spectra.env.ACTLOG_PASSWORD`.
  - Brand `Acme Corp {runId}-012`, dibuat lewat API oleh akun aktor (entri User Action `Create` `Brand`). Object `Brand` ini menjadi nilai pembanding pada daftar opsi Object (langkah 19).
  - Aktivitas Fixed Asset (`Register Asset`) dengan nama aset `Forklift FA {runId}-012` dan aktivitas Supply Asset dengan nama `Supply SAMS {runId}-012` pada entitas yang sama, dibuat lewat API modul FAMS dan SAMS oleh akun aktor.
- Kemampuan teknis (disediakan tim FE/BE): (a) sesi produk (card Fixed Asset, Admin Console, Global Settings) dibuka oleh user uji lewat alur Auth tanpa UI; (b) aksi FAMS dan SAMS lewat API pada entitas yang sama.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user `John Doe {runId}-012` dan `Rudi Hartono {runId}-012`, Brand `Acme Corp {runId}-012`, serta aset `Forklift FA {runId}-012` dan `Supply SAMS {runId}-012` bila masih ada.

## Test Steps

### TC-GS-ACTLOG-38: Tab Session hanya memuat event platform dan event sesi Global Settings

1. Buka Global Settings > Activity Log > Session
2. Ketik Search `John Doe {runId}-012`, tekan Enter
3. Verifikasi entri Login platform milik `John Doe {runId}-012` tampil pada tabel sebelum filter diterapkan
4. Klik icon Filter, pilih Activity `Session`, klik [Apply]
5. Verifikasi hanya satu baris `Session started` milik `John Doe {runId}-012` yang tampil, yaitu entri sesi Global Settings
6. Verifikasi entri sesi Fixed Asset dan entri sesi Admin Console milik `John Doe {runId}-012` tidak tampil
7. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-GS-ACTLOG-39: Tab Session memuat login semua user entitas, termasuk user tanpa akses Global Settings

8. Ketik Search `Rudi Hartono {runId}-012`, tekan Enter
9. Verifikasi baris Login `Success` milik `Rudi H` tampil di tab Session
10. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-GS-ACTLOG-40: Tab User Action hanya memuat aksi modul Global Settings

11. Klik Tab `User Action`
12. Ketik Search `Acme Corp {runId}-012`, tekan Enter
13. Verifikasi baris `Create` `Brand` `Acme Corp {runId}-012` tampil
14. Ganti isi kotak search dengan `Forklift FA {runId}-012`, tekan Enter
15. Verifikasi tidak ada baris dari Fixed Asset untuk `Forklift FA {runId}-012`
16. Ganti isi kotak search dengan `Supply SAMS {runId}-012`, tekan Enter
17. Verifikasi tidak ada baris dari Supply Asset untuk `Supply SAMS {runId}-012`
18. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel, klik icon Filter, buka daftar opsi Object
19. Verifikasi daftar opsi Object memuat `Brand`
20. Verifikasi daftar opsi Object tidak memuat `Register Asset` dan `Supply Asset`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-38, 39, 40).
- Langkah penghubung (tanpa awalan `Verifikasi`): mengetik Search `John Doe {runId}-012` pada langkah 2 agar baris subjek ditemukan di antara baris run lain, serta pemulihan state antar TC (langkah 7, 10, dan 18: Clear Field filter dan menutup Search lewat `(←)`). Langkah 8, 12, 14, dan 16 memakai Search nama data milik spec ini sebagai cara mengamati baris subjek, Brand, Fixed Asset, dan Supply Asset karena TC hanya menyebut "amati baris".
- Asersi tidak adanya baris Fixed Asset dan Supply Asset (langkah 15 dan 17) memakai anchor positif langkah 13 (baris Brand tampil pada surface yang sama) dan terbatas pada hasil Search terhadap data milik spec ini.
- Anchor tambahan yang tidak ada di TC (S-03): langkah 19 (opsi `Brand` tampil pada daftar opsi Object) mendahului langkah 20 (opsi `Register Asset` dan `Supply Asset` tidak ada), supaya ketiadaan opsi bukan karena daftar belum termuat; langkah 20 adalah penerjemahan konkret Expected c TC-GS-ACTLOG-40.
- Langkah 5 mengasersi jumlah (tepat satu baris `Session started` meski tiga sesi produk dibuka) dan bukan asersi absence kelas g; langkah 3 menjadi anchor positif (Login platform tampil sebelum filter).
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 4 mengikuti TC-GS-ACTLOG-38 dan langkah klik icon Filter pada langkah 7 dan 18 (langkah penghubung pemulihan) bergantung pada perilaku itu.
  - TC-GS-ACTLOG-38 menyebut "entri Session Global Settings `Session started` milik John Doe pada waktu yang berbeda" tanpa cara membedakan entri sesi Global Settings dari Fixed Asset dan Admin Console di tabel selain jumlah baris; spec mengasersi jumlah satu baris.
  - TC-GS-ACTLOG-39 menulis Search `Rudi` dengan hasil `Rudi H`; spec memakai Search `Rudi Hartono {runId}-012` agar baris run ini terpisah dari sisa run lain.
  - TC-GS-ACTLOG-40 tidak menyebut nama aset FAMS dan SAMS maupun cara mengamati ketiadaan baris; spec memakai nama aset bersuffix dan Search.
  - TC-GS-ACTLOG-40 Expected c ("hanya memuat nilai dari modul Global Settings yang ada pada data") tidak punya daftar nilai yang pasti; spec mengasersi `Brand` ada serta `Register Asset` dan `Supply Asset` tidak ada. Nilai Object lain pada daftar tidak diasersi.
