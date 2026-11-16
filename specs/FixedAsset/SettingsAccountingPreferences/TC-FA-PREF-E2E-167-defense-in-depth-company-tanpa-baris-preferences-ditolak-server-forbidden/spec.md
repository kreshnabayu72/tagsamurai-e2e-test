---
id: TC-FA-PREF-E2E-167-defense-in-depth-company-tanpa-baris-preferences-ditolak-server-forbidden
title: "Defense-in-depth: Company Tanpa Baris Preferences Ditolak Server dengan Forbidden pada Request Langsung dan Pembukaan Tab"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-276
  - TC-FA-PREF-562
sourceRules: ["F-FAPREF-02.k4", "FAPREF-LOGIC-01b", "E-FAPREF-12"]
smoke: []
dependsOn: []
trace:
  "F-FAPREF-02.k4": 2
  "FAPREF-LOGIC-01b": 4
  "E-FAPREF-12": [6, 9]
anchor: [7, 8]
coverage:
  web: automated
---

# Defense-in-depth: Company Tanpa Baris Preferences Ditolak Server dengan Forbidden pada Request Langsung dan Pembukaan Tab

## Prerequisites

- Mode: FE+BE.
- Kelas harness: a (defense-in-depth, penolakan server).
- Akun aktor: Total Control company client yang modul akuntansinya aktif tetapi belum memiliki baris Preferences (Pre-setup PB-11 untuk TC-FA-PREF-276 dan PC-13 untuk TC-FA-PREF-562); email akun ini tidak tertulis di Pre-setup TC (disediakan tim FE, lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini dengan akun di atas; hook `after` mengembalikan sesi ke akun default suite. Pengecualian layar awal: company tidak memiliki baris Preferences sehingga membuka tab Preferences ditolak server; hook `beforeEach` suite hanya menutup dialog dan halaman Preferences dibuka pada langkah 5.
- Data Pre-setup: company tanpa baris Preferences (seed disediakan tim FE/BE, lihat `suite.md`, butir seed dan pemulihan lewat API). Spec tidak mengubah state company; tidak ada baris Preferences yang dibuat.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung ke server memakai sesi API Total Control company tersebut (butir "Sesi API aktor" di `suite.md`); fixture BE untuk membaca ada atau tidaknya baris Preferences company; pengamatan respons jaringan dari browser (hanya mengamati, tanpa mengubah respons) untuk status respons pembacaan pada langkah 6; alamat tautan langsung Settings > Accounting > Preferences ditetapkan tim FE karena TC tidak menyebutnya.
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) untuk akun aktor spec ini.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-276: Permintaan langsung ke Preferences company tanpa baris Preferences ditolak server Forbidden

1. Kirim permintaan baca Preferences langsung ke server memakai sesi API Total Control company tanpa baris Preferences
2. Verifikasi server menolak permintaan dengan Forbidden (403)
3. Baca status baris Preferences company lewat fixture BE
4. Verifikasi tidak ada baris Preferences yang dibuat

### TC-FA-PREF-562: Membuka tab Preferences saat company belum memiliki baris Preferences ditolak server

5. Buka Settings > Accounting > Preferences lewat URL langsung
6. Verifikasi respons pembacaan Preferences Forbidden (403)
7. Verifikasi toast "You don't have permission to do this." tampil
8. Verifikasi halaman tidak dialihkan
9. Verifikasi nilai Preferences tidak ditampilkan

## Notes

- K-1: TC-FA-PREF-276 (kelas a) memiliki Expected berupa respons API dan state data; tetap masuk spec FE+BE walau tumpang tindih dengan `tc-[modul]-backend.md` (bagian 3 prinsip 13a). TC-FA-PREF-562 memuat penolakan server yang sama pada jalur UI sehingga ditaruh bersama.
- Langkah 6 mengasersi status respons lewat pengamatan jaringan, bukan perilaku FE pada request langsung (bagian 8b butir 1); toast pada langkah 7 adalah perilaku FE atas respons itu dan berasal dari Expected TC-FA-PREF-562 butir b. Langkah 9 (absence) memakai toast pada langkah 7 sebagai anchor positif (bagian 8b butir 2).
- TC defense-in-depth lain pada company yang memiliki baris Preferences (TC-FA-PREF-232, 544, 545) ada di spec 084.
- Temuan untuk QA:
  - TC-FA-PREF-276 memakai company PB-11 dan TC-FA-PREF-562 memakai company PC-13 (dua seri fixture berbeda); spec mengasumsikan keduanya setara (company client dengan modul akuntansi aktif tanpa baris Preferences) dan memakai satu akun. Email Total Control company ini tidak tertulis di tabel Pre-setup.
  - TC-FA-PREF-276 Post Condition ("Company tetap tanpa baris Preferences") tidak punya langkah observasi sendiri di TC; Expected b ("Tidak ada baris Preferences yang dibuat") diasersi pada langkah 3 dan 4.
  - TC-FA-PREF-562 tidak menyebut alamat URL langsung.
