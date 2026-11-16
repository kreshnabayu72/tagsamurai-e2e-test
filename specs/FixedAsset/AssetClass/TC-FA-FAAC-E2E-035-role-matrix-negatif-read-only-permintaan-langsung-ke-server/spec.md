---
id: TC-FA-FAAC-E2E-035-role-matrix-negatif-read-only-permintaan-langsung-ke-server
title: "Role Matrix Negatif: Read Only Tidak Dapat Create, Edit, Deactivate, atau Delete (UI dan Permintaan Langsung ke Server)"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-595
  - TC-FA-FAAC-596
  - TC-FA-FAAC-597
sourceRules: ["§4.8#r3", "§4.8#r11", "§4.8#r16", "§4.8#r18", "E-FAAC-78", "§9.3#r2", "ST-32", "§3.9#r8", "§4.8#r9", "§4.8#b2", "§4.8#r10", "§9.3#r3", "§4.8#r20", "§9.3#r4"]
smoke: []
dependsOn: []
trace:
  "§4.8#r3": [1, 22]
  "§4.8#r11": 2
  "§4.8#r16": [3, 23]
  "§4.8#r18": 3
  "E-FAAC-78": [6, 7, 17, 18, 19, 20, 26, 27, 28]
  "§9.3#r2": 6
  "ST-32": 10
  "§3.9#r8": 10
  "§4.8#r9": 13
  "§4.8#b2": 13
  "§4.8#r10": 14
  "§9.3#r3": [17, 18]
  "§4.8#r20": 23
  "§9.3#r4": 26
coverage:
  web: automated
---

# Role Matrix Negatif: Read Only Tidak Dapat Create, Edit, Deactivate, atau Delete (UI dan Permintaan Langsung ke Server)

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Read Only) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Read Only | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_RO_PASSWORD` | TC-FA-FAAC-595, TC-FA-FAAC-596, TC-FA-FAAC-597 |

- Env var: `FA_AC_RO_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Asset Class B-ANCHOR (Anchor Heavy Equipment, Active; seed Pre-setup, dependensi TC-FA-FAAC-87 dijalankan lewat seeding API). Dibaca, tidak diubah; permintaan yang ditolak tidak mengubah data. Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat, mengubah, atau menghapus data.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: klien HTTP yang menyertakan sesi aktor ini (kemampuan disediakan tim FE/BE; endpoint dan bentuk request tidak didefinisikan di TC, PRD, atau LLD yang dibaca); kemampuan baca BE untuk jumlah Asset Class dan state B-ANCHOR (keberadaan, Class Name, status Active); hover pada elemen dan membaca tooltip.

## Test Steps

### TC-FA-FAAC-595

1. Verifikasi Table Tools (Search, Filter, Download, Changelog) dan tabel Asset Class tampil
2. Verifikasi Button [+ Asset Class] dan link "Use recommended classes" Hidden
3. Verifikasi tombol ⋯ per baris Hidden (row action Duplicate tidak tersedia)
4. Catat baseline lewat kemampuan baca BE (disediakan tim FE/BE): jumlah Asset Class
5. Kirim permintaan Create Asset Class langsung ke server tanpa melewati browser
6. Verifikasi respons server atas permintaan Create Asset Class ditolak dengan status 403
7. Verifikasi jumlah Asset Class tidak berubah dibanding baseline

### TC-FA-FAAC-596

8. Ketik Search `B-ANCHOR`, tekan Enter
9. Arahkan kursor ke toggle Active baris B-ANCHOR
10. Verifikasi toggle kolom Active Disabled dengan tooltip "You don't have permission to edit."
11. Klik Class Code B-ANCHOR untuk membuka Detail mode Edit
12. Arahkan kursor ke field Class Name pada tab General
13. Verifikasi field Detail mode Edit Disabled dengan tooltip "You don't have permission to edit."
14. Verifikasi Button [Save] dan [Clear Field] Hidden
15. Catat baseline lewat kemampuan baca BE (disediakan tim FE/BE): Class Name dan status Active B-ANCHOR
16. Kirim permintaan Edit dan permintaan Deactivate Asset Class B-ANCHOR langsung ke server tanpa melewati browser
17. Verifikasi respons server atas permintaan Edit ditolak dengan status 403
18. Verifikasi respons server atas permintaan Deactivate ditolak dengan status 403
19. Verifikasi Class Name B-ANCHOR tidak berubah dibanding baseline
20. Verifikasi status Active B-ANCHOR tidak berubah dibanding baseline
21. Kembali ke tabel Asset Class lewat Breadcrumb Asset Class (form tidak diubah)

### TC-FA-FAAC-597

22. Verifikasi Table Tools (Search, Filter, Download, Changelog) dan tabel Asset Class tampil
23. Verifikasi tombol ⋯ per baris Hidden sehingga row action Delete tidak tersedia
24. Catat baseline lewat kemampuan baca BE (disediakan tim FE/BE): jumlah Asset Class dan keberadaan B-ANCHOR
25. Kirim permintaan Delete Asset Class B-ANCHOR langsung ke server tanpa melewati browser
26. Verifikasi respons server atas permintaan Delete ditolak dengan status 403
27. Verifikasi keberadaan Asset Class B-ANCHOR tidak berubah dibanding baseline
28. Verifikasi jumlah Asset Class tidak berubah dibanding baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec defense-in-depth (kelas a) untuk satu role (Read Only): UI diasersi Hidden atau Disabled, lalu permintaan langsung ke server diasersi ditolak 403. Satu akun, tanpa ganti akun.
- `K-1`: TC defense-in-depth dengan Expected respons API (status respons dan state data lewat fixture BE) tetap masuk spec FE+BE walau tumpang tindih dengan dokumen TC BE; TC granular tetap sumber dan tiap TC tepat satu spec.
- Pembagian TC lintas spec (S-05): TC-595, TC-596, dan TC-597 ada di spec ini (UI, status respons 403, dan state data) dan di spec 193 (klausa "tidak ada entri baru di Changelog Asset Class, System Log, maupun Activity Log" dengan permintaan yang sama sebagai pemicu serta baseline log sendiri). Spec ini tidak mengasersi log.
- Bagian 8b butir 1: langkah permintaan langsung ke server hanya mengasersi respons (status) dan state data lewat kemampuan baca BE; perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 (Search untuk menemukan baris target, R-16) dan langkah 21 (kembali ke tabel dari Detail B-ANCHOR, S-09).
- Baseline state dicatat ulang sebelum aksi pemicu tiap TC (langkah 4, 15, dan 24) dan asersi memakai perbandingan terhadap baseline TC itu (S-12).
- Asersi Hidden UI didahului `Verifikasi` Table Tools dan tabel tampil sebagai anchor positif permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAC-595 menyebut link "Use recommended classes" Hidden, tetapi link itu hanya ada pada EmptyState tabel kosong sedangkan precondition tidak menyebut tabel kosong; asersi Hidden-nya tidak membuktikan apa pun bila tabel berisi.
  - Endpoint dan bentuk permintaan langsung ke server tidak disebut TC maupun PRD; ditulis sebagai kemampuan yang disediakan tim FE/BE (S-13).
