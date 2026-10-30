---
id: TC-GS-ROLE-E2E-059-download-lebih-5000-baris-background-job
title: "Download Tab Total Control di Atas 5.000 Baris Berjalan sebagai Background Job"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-180
coverage:
  web: automated
---

# Download Tab Total Control di Atas 5.000 Baris Berjalan sebagai Background Job

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; berkas dibuat oleh job latar di backend nyata.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > Total Control dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data volume khusus (kelas e, prinsip 13e konvensi): Tab Total Control berisi lebih dari 5.000 user (Pre-setup #17, disiapkan lewat seed data volume). Mekanisme seeding volume dan pembersihannya disediakan tim FE/BE (TC tidak mendefinisikannya, lihat Temuan untuk QA); seeding dilakukan di hook `before` dan dibersihkan di hook `after` yang tetap jalan walau spec gagal di tengah. Data volume tidak dipakai spec lain, sehingga suite berjalan serial.
- Data uji: format `CSV`.
- Kemampuan teknis: membaca jumlah notifikasi dan isi (tombol) item Notification Center; menunggu job latar selesai sampai batas waktu yang disediakan tim FE/BE (waktu job tergantung volume seed).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission, Tab Total Control.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-180: Download lebih dari 5.000 baris berjalan sebagai background job

1. Catat jumlah notifikasi di Notification Center sebagai baseline
2. Klik icon Download
3. Klik `Download as CSV`
4. Verifikasi toast informational tampil saat trigger
5. Verifikasi halaman tidak terkunci
6. Tunggu job latar selesai
7. Buka Notification Center
8. Verifikasi jumlah notifikasi bertambah satu dari baseline
9. Verifikasi notifikasi baru berisi tombol `[Download]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE. Kelas e (volume data, lebih dari 5.000 baris) sesuai rencana; job latar dan notifikasi diamati sebagai bagian dari TC yang sama dan tidak ada TC lain di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (baseline jumlah notifikasi, supaya notifikasi baru dapat dibedakan dari notifikasi lama), langkah 6 (menunggu job selesai), dan langkah 7 (membuka Notification Center).
- Asersi tambahan (konkretisasi Expected): langkah 8 membandingkan jumlah notifikasi dengan baseline pada langkah 1 (baseline pembeda notifikasi baru dari yang lama).
- Pembagian TC lintas spec: TC-GS-ROLE-174 sampai 178 (Download Tab Total Control dan Read Only dengan volume lazim) di spec 058; TC-GS-ROLE-179 (Download gagal) di spec 069.
- Temuan untuk QA:
  - TC-GS-ROLE-180 bertentangan dengan `foundation/process/prd-process/error-handling-convention.md` §10.1 (dirujuk PRD role.md §5 Download): Download di atas 5.000 baris memakai loading screen sampai berkas siap lalu langsung terunduh, tanpa job latar, toast informasional, atau notifikasi in-app. Spec mengikuti Expected TC; QA perlu menyelaraskan TC atau PRD.
  - TC-GS-ROLE-180 Expected a: teks toast informational tidak disebut; spec hanya mengasersi toast tampil. "Halaman tidak terkunci" tidak didefinisikan; spec mengasersinya sebagai satu `Verifikasi`.
  - TC-GS-ROLE-180: mekanisme seed data volume (lebih dari 5.000 user Total Control) dan batas waktu tunggu job tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE. TC juga tidak meminta berkas dibuka atau dibaca, sehingga isi berkas tidak diasersi.
