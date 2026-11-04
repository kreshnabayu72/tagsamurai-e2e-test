---
id: TC-AC-SU-E2E-187-double-click-dan-double-submit-checkbox-resend-dan-save-group-role
title: "Double-Click dan Double-Submit pada Checkbox CRUD, Resend Activation Email, dan Save Popup Assign Group Role Hanya Memproses Satu Request"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-193
  - TC-AC-SU-630
  - TC-AC-SU-631
  - TC-AC-SU-632
coverage:
  web: automated
---

# Double-Click dan Double-Submit pada Checkbox CRUD, Resend Activation Email, dan Save Popup Assign Group Role Hanya Memproses Satu Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec (Region B dari Group Tree Pre-setup hanya menjadi target assignment dan tidak diubah):

| Kode | Name | Email | State awal |
|---|---|---|---|
| A | `Budi Santoso {runId}-187A` | `budisantoso+{runId}-187a@qwertysystem.net` | Activated, tanpa tier, bukan Group Manager; "Manage device master data" ON dengan C unchecked (TC-193) |
| B | `Sarah Lee {runId}-187B` | `sarahlee+{runId}-187b@qwertysystem.net` | Pending Activation, di luar cooldown Resend (TC-630) |
| C | `Mike Tan {runId}-187C` | `miketan+{runId}-187c@qwertysystem.net` | Activated, tanpa tier, "Manage partner" aktif di Region A (TC-631) |
| D | `Mike Tan {runId}-187D` | `miketan+{runId}-187d@qwertysystem.net` | Activated, tanpa tier, "Manage group" aktif dengan Update unchecked (TC-632) |

- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons request sampai dilepas (penahanan hanya untuk mengamati state Loading; bukan kegagalan, sehingga bukan kelas b); Fixture BE. Tahanan dilepas segera sesudah asersi Loading (S-09). Tanpa jam server.
- Langkah "Tunggu aksi selesai" memakai polling tiap 5 detik sampai tombol atau kontrol aktif kembali, batas tunggu 30 detik.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-193: Klik checkbox berulang cepat
1. Ketik Search `Budi Santoso {runId}-187A`, tekan Enter, klik Name baris A, klik Tab Role, lalu sub-tab Global Role
2. Double-click cepat checkbox C pada baris `Manage device master data`
3. Tunggu aksi selesai, lalu catat keadaan checkbox C sebagai K1, muat ulang halaman, dan buka kembali Tab Role
4. Verifikasi keadaan checkbox C sama dengan K1 (sama dengan tampilan setelah request selesai)
5. Klik Tab Changelog
6. Verifikasi Tab Changelog memuat sedikitnya satu entri untuk perubahan checkbox C `Manage device master data`
7. Verifikasi Tab Changelog tidak memuat dua entri dengan Field, Old Value, dan New Value yang identik (tanpa entri ganda)
### TC-AC-SU-630: Double-submit Resend Activation Email
8. Klik menu Settings > User di sidebar, lalu ketik Search `Sarah Lee {runId}-187B`, tekan Enter
9. Buka row action (⋯) baris B, tahan respons request Resend, lalu klik Resend Activation Email dua kali secepatnya
10. Verifikasi kontrol Resend Activation Email masuk state loading atau disabled setelah klik pertama
11. Lepas tahanan respons, lalu klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
12. Ketik Search `Sarah Lee {runId}-187B` pada Popup Changelog: User, tekan Enter; tutup dan buka ulang popup tiap 5 detik sampai entri muncul (batas tunggu 30 detik)
13. Verifikasi hanya 1 entri log baru untuk B (Action `Resend Activation Email`)
### TC-AC-SU-631: Double-submit Save popup Assign Group Role
14. Tutup popup, ganti isi kotak search dengan `Mike Tan {runId}-187C`, tekan Enter, klik Name baris C, klik Tab Role, lalu sub-tab Group Role
15. Klik `[Assign Group]` pada baris "Manage partner", klik `[+ Assign Group]`, centang Region B, lalu klik `[Select]`
16. Tahan respons request Save assignment, lalu klik `[Save]` dua kali secepatnya
17. Verifikasi tombol `[Save]` masuk state loading atau disabled setelah klik pertama
18. Lepas tahanan respons
19. Tunggu aksi selesai
20. Klik menu Settings > User di sidebar, lalu klik icon Changelog di toolbar
21. Ketik Search `Mike Tan {runId}-187C` pada Popup Changelog: User, tekan Enter
22. Verifikasi hanya 1 entri log baru untuk C (Action `Assign`, Field `Manage partner — Region B — Access`)
### TC-AC-SU-632: Double-submit autosave checkbox CRUD
23. Tutup popup, ketik Search `Mike Tan {runId}-187D`, tekan Enter, klik Name baris D, klik Tab Role, lalu sub-tab Global Role
24. Tahan respons request simpan permission, lalu double-click cepat checkbox Update pada "Manage group"
25. Verifikasi checkbox Update masuk state loading atau disabled setelah klik pertama
26. Lepas tahanan respons
27. Tunggu aksi selesai
28. Klik menu Settings > User di sidebar, lalu klik icon Changelog di toolbar
29. Ketik Search `Mike Tan {runId}-187D` pada Popup Changelog: User, tekan Enter
30. Verifikasi hanya 1 entri log baru untuk D (Action `Edit`, Field `Manage group — Update`)

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), pemuatan ulang halaman, menahan dan melepas respons, polling Popup Changelog: User pada TC-630 (batas tunggu 30 detik, entri Resend ditulis di background), dan menutup popup. Asersi state Loading ditulis sebelum tahanan dilepas (bagian 8b butir 5). User bernama unik sehingga baseline entri nol dan "1 entri log baru" menjadi asersi jumlah (bukan absence kelas g).
- Empat blok berpola sama (satu kontrol diklik dua kali, state loading, hasil tunggal) dan berdiri sendiri pada user seeding sendiri; 30 langkah wajar.
- Temuan untuk QA:
  - TC-193 butir a dan butir b mensyaratkan "status akhir sama dengan tampilan setelah request selesai" dan "tepat 1 entri per perubahan yang benar-benar tersimpan" tanpa menyatakan apakah dua klik menghasilkan satu atau dua perubahan; spec mengasersi keadaan akhir konsisten setelah muat ulang dan tidak adanya entri identik ganda.
  - TC-630 sampai TC-632 menyebut "Buka surface terkait" tanpa menyebut surface; spec memakai row action Resend, popup Assign Group Role, dan Tab Role Global Role pada Settings > User. TC-630 tidak menyatakan apakah menu row action masih terbuka untuk klik kedua.
  - TC-630 sampai TC-632 butir a menyebut "tombol/kontrol" tanpa menyebut elemen yang di-disable; spec mengasersi kontrol yang diklik.
  - TC memakai nama literal (`Budi Santoso`, `Sarah Lee`, `Mike Tan`); spec memakai nama bersuffix (S-12).
