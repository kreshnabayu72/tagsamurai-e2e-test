---
id: TC-FA-SU-E2E-399-defense-in-depth-baris-pola-group-manager-ditolak-403-baris-manage-user-role-diterima-dan-konfirmasi-auto-revert-409
title: "Defense-in-depth Baris Pola Group Manager: Ditolak 403, Baris Manage user & role Diterima, dan Konfirmasi Auto-Revert 409"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-1099
coverage:
  web: automated
---

# Defense-in-depth Baris Pola Group Manager: Ditolak 403, Baris Manage user & role Diterima, dan Konfirmasi Auto-Revert 409

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; Group Role Manage user & role pada Finance & Accounting, Read dan Update), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`; email tidak tertulis di Pre-setup TC (disediakan tim FE). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor berikutnya (ganti akun eksplisit, S-07; sesi API untuk klien HTTP): langkah 12 Manage global user & role (Update) Qori Akbar (Pre-setup #4), `Spectra.env.FA_MURG_UPD_PASSWORD`; langkah 16 Default User Ahmad Dahlan (Pre-setup #2), `Spectra.env.FA_DU_PASSWORD`. Email Qori Akbar tidak tertulis di Pre-setup TC (disediakan tim FE).
- Hook suite (`suite.md`): flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan Group Manager `FaUserGM` (#48). Target: Putri Anggraeni (Group Manager Finance & Accounting, turunan Accounts Payable; baris pola Group Manager pada kedua node; Group Role Manage user & role pada Finance & Accounting). Nama pengguna dan grup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): klien HTTP dengan token sesi API aktor yang sedang aktif untuk permintaan langsung ke server. Pembacaan state data (CRUD baris pola dan baris Manage user & role, keberadaan baris Transaction Role pola, grup pada baris pola, status Group Manager Putri) lewat endpoint baca dari tim BE memakai sesi API Total Control Lina Marlina (Pre-setup #1, `Spectra.env.FA_TC_PASSWORD`). Nama dan bentuk penanda konfirmasi Auto-Revert pada permintaan langkah 20 mengikuti kontrak `settings-user/API/roles.md`, disediakan tim BE (belum diverifikasi).
- Kemampuan seed API (disediakan tim BE/FE): memulihkan CRUD baris, status Group Manager, dan baris pola Putri Anggraeni ke kondisi Pre-setup #48. Dijalankan sebagai langkah penghubung terakhir dan di hook `after` (cadangan).
- State yang diubah dan pemulihannya: langkah 8 menyimpan perubahan CRUD baris Manage user & role × Finance & Accounting milik Putri; langkah 20 melepas status Group Manager Putri dan mempertahankan baris pola sebagai baris biasa (Last Updated dan Modified By berubah, entri log permanen bertambah). Dipulihkan ke Pre-setup #48 lewat seed API. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat state awal lewat API: CRUD baris pola Manage files × Accounts Payable, keberadaan baris pola Transaction Role Transfer × Approver (grup dalam subtree), grup pada baris pola Disposal × Asset Admin, CRUD baris Manage user & role × Finance & Accounting, dan status Group Manager Putri Anggraeni

### Langkah 1 dan 2 TC: permintaan ditolak 403 oleh Sinta Dewi

2. Kirim permintaan langsung ke API ubah CRUD baris pola Manage files × Accounts Payable milik Putri Anggraeni memakai klien HTTP dengan token Sinta Dewi
3. Verifikasi server menolak permintaan dengan status 403
4. Verifikasi CRUD baris pola Manage files × Accounts Payable milik Putri Anggraeni tidak berubah dari state awal (dibaca lewat API)
5. Kirim permintaan langsung hapus baris Transaction Role pola Transfer × Approver (grup dalam subtree) milik Putri Anggraeni memakai klien HTTP dengan token Sinta Dewi
6. Verifikasi server menolak permintaan dengan status 403
7. Verifikasi baris Transaction Role pola Transfer × Approver milik Putri Anggraeni masih ada (dibaca lewat API)

### Langkah 4 TC: baris Manage user & role diterima

8. Kirim permintaan langsung ke API ubah CRUD baris Manage user & role × Finance & Accounting milik Putri Anggraeni memakai klien HTTP dengan token Sinta Dewi
9. Verifikasi server menerima permintaan (respons sukses, bukan 403)
10. Verifikasi CRUD baris Manage user & role × Finance & Accounting milik Putri Anggraeni tersimpan sesuai permintaan (dibaca lewat API)
11. Verifikasi status Group Manager Putri Anggraeni tidak berubah, tanpa auto-revert (dibaca lewat API)

### Langkah 3 TC: permintaan ditolak 403 oleh Qori Akbar

12. Ganti akun: login API sebagai Qori Akbar (Manage global user & role, `Spectra.env.FA_MURG_UPD_PASSWORD`) untuk klien HTTP
13. Kirim permintaan langsung ke API cabut Accounts Payable dari baris pola Disposal × Asset Admin milik Putri Anggraeni memakai klien HTTP dengan token Qori Akbar
14. Verifikasi server menolak permintaan dengan status 403
15. Verifikasi Accounts Payable tetap pada baris pola Disposal × Asset Admin milik Putri Anggraeni (dibaca lewat API)

### Langkah 5 TC: konfirmasi Auto-Revert oleh Default User

16. Ganti akun: login API sebagai Ahmad Dahlan (Default User, `Spectra.env.FA_DU_PASSWORD`) untuk klien HTTP
17. Kirim permintaan langsung ke API ubah CRUD baris pola Manage files × Accounts Payable milik Putri Anggraeni tanpa penanda konfirmasi Auto-Revert memakai klien HTTP dengan token Ahmad Dahlan
18. Verifikasi server menolak penyimpangan dengan status 409 yang meminta konfirmasi Auto-Revert
19. Verifikasi tidak ada yang tersimpan: CRUD baris pola Manage files × Accounts Payable dan status Group Manager Putri Anggraeni tidak berubah (dibaca lewat API)
20. Ulangi permintaan langkah 17 dengan penanda konfirmasi Auto-Revert
21. Verifikasi perubahan CRUD baris pola Manage files × Accounts Payable tersimpan (dibaca lewat API)
22. Verifikasi status Group Manager Putri Anggraeni terlepas (dibaca lewat API)
23. Verifikasi baris pola Group Manager Putri Anggraeni tetap tersimpan sebagai baris biasa (dibaca lewat API)
24. Pulihkan CRUD baris, status Group Manager, dan baris pola Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke langkah TC-FA-SU-1099. Login pertama TC (Sinta Dewi) dilakukan hook `before`.
- K-1 dan bagian 8b butir 1: TC-FA-SU-1099 berformat Expected respons API (status respons dan state data lewat API); TC tetap masuk spec FE+BE walau tumpang tindih dengan pengujian tingkat endpoint, dan asersi spec hanya status respons dan state data. Pemeriksaan "Tab Changelog" pada langkah 6 TC adalah asersi tampilan dan tidak dijalankan di spec permintaan langsung; kejadian log diamati di spec 400.
- S-05: klausa "tidak ada entri log" pada Expected a TC-FA-SU-1099 (langkah 1 sampai 3 TC) diasersi di spec 400 (kelas g) dengan permintaan yang sama sebagai pemicu, user dan baseline sendiri; spec ini hanya mengasersi status respons dan state data (`[KEPUTUSAN 2026-10-30]`). Id TC tetap di `sourceTc` kedua spec.
- Urutan langkah TC diubah (langkah 1, 2, 4, 3, 5) supaya ganti akun hanya dua kali (Sinta Dewi, Qori Akbar, Ahmad Dahlan); langkah 8 sampai 11 tidak memengaruhi baris yang diuji langkah 13 dan 17.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (baca state awal), 12 dan 16 (ganti akun eksplisit, S-07), dan 24 (pemulihan seed API).
- Temuan untuk QA:
  - Kontrak API belum diverifikasi: nama penanda konfirmasi Auto-Revert dan kode 403 untuk langkah 1 sampai 3 serta 409 untuk langkah 5 tertulis di TC dengan catatan "kontrak `settings-user/API/roles.md` perlu diverifikasi"; spec mengasersi kode seperti tertulis di TC tanpa menyebut nama penanda atau endpoint (S-13).
  - Langkah 6 TC ("Periksa nilai tersimpan lewat API dan Tab Changelog") membutuhkan endpoint baca dari tim BE; endpoint dan bentuk responsnya tidak ditulis di TC, PRD, atau LLD yang dirujuk.
  - Payload "ubah CRUD" (kolom apa, ke nilai apa) tidak ditentukan TC; ditentukan saat tahap script.
  - Belum jelas apakah penyimpanan langkah 4 (baris Manage user & role) mencatat entri `Edit` pada Tab Changelog; Expected b tidak menyebut log dan Tab Changelog tidak diasersi.
  - Pre-setup TC (kolom precondition c) mencantumkan #2, #4, #6, #20, #21, #23, #48, tetapi tidak memberi email dan nama env password Putri Anggraeni, Sinta Dewi, dan Qori Akbar; Putri hanya target sehingga tidak butuh password.
  - Expected c menyebut "status GM terlepas, dan baris pola dipertahankan sebagai baris biasa" tanpa menyebut baris mana; spec mengasersi status dan keberadaan baris pola secara umum.
  - Post Condition "Putri dipulihkan ke state Pre-setup #48 oleh automation baseline" tidak punya langkah observasi dan tidak diasersi; spec menjalankan pemulihan lewat seed API (langkah 24).
