---
id: TC-FA-LBL-E2E-010-provenance-label-default-otomatis-dan-promosi-manual-ke-default
title: "Provenance label: Default Label otomatis, promosi manual ke default, dan relasi default tidak dapat dilepas dari Asset Detail"
priority: High
caseType: Positive
status: draft
sourceRules:
  - FALB-LOGIC-04a
  - FALB-LOGIC-04b
  - E-FALB-05
  - F-FALB-07
  - E-FALB-13
  - FALB-LOGIC-04f
  - FALB-LOGIC-06c
  - F-FALB-11.k3
coverage:
  web: automated
---

# Provenance label: Default Label otomatis, promosi manual ke default, pelepasan dan Bulk Remove

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji, semuanya bersuffix `{runId}-010`, dibuat lewat API di hook `before` dan dihapus di hook `after` (aset, Asset Name, lalu label):
  - `DU-53`: label seed utama (`Seed-{runId}-010`), Default Label dari Asset Name `DU-27`.
  - `DU-27`: Asset Name yang memakai label seed `DU-53` sebagai Default Label; aset default `DU-27` adalah aset Active dari Asset Name itu, sehingga memegang relasi `default` untuk label `DU-53`.
  - `DU-54`: label seed manual untuk skenario `E-FALB-13` (`Manual-{runId}-010`) yang menempel manual pada aset manual `DU-29`.
  - `DU-29`: aset manual skenario `E-FALB-13` (aset Active dari Asset Name `DU-29` yang belum memiliki Default Label; Asset Name itu memiliki Total Asset lebih dari 0 karena aset manual `DU-29`); Asset Name itu lalu menetapkan label `DU-54` sebagai Default Label.
  - `DU-26`: seluruh aset Active spec ini (aset default `DU-27` dan aset manual `DU-29`, dua aset).
  - Penamaan objek: `DU-27` menamai Asset Name (nama Asset Name bersuffix `{runId}-010`), dan "aset default `DU-27`" adalah aset Active pertama di dalam Asset Name itu; `DU-29` menamai Asset Name skenario `E-FALB-13`, dan "aset manual `DU-29`" adalah aset Active di dalamnya. Bila sebuah langkah menyebut `DU-27` atau `DU-29` tanpa jenis objek, artinya Asset Name pada langkah yang bekerja di tab Asset Name, dan aset di dalamnya pada langkah yang bekerja di Asset List atau Asset Detail.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, Asset Name, dan aset, disediakan tim FE/BE. Halaman Asset List dan Asset Detail dimiliki modul `asset/`. Langkah 8 sampai 16 (tab Asset Name dan Modal Edit Asset Name) bergantung pada PRD `settings-asset-name` dan dikutip di `## Notes`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB-LOGIC-04a: Setiap relasi aset dan label memiliki asal-usul default atau manual

1. Ketik Search `DU-26`, tekan Enter
2. Buka Asset Detail aset manual `DU-29` dari Asset List modul `asset/`
3. Verifikasi chip label `DU-54` tampil dengan ikon `[✕]`
4. Buka Asset Detail aset default `DU-27`
5. Verifikasi chip label `DU-53` tampil tanpa ikon `[✕]`

### FALB-LOGIC-04b: Relasi default ditugaskan otomatis lewat Default Label pada template Asset Name

6. Verifikasi chip label `DU-53` tampil pada Asset Detail aset default `DU-27` yang dibuat dari Asset Name `DU-27`

### E-FALB-05: Label bersumber default tidak dapat dilepas dari Asset Detail

7. Verifikasi ikon `[✕]` tidak tampil pada chip label `DU-53` di Asset Detail aset default `DU-27`

### F-FALB-07: Master label tersedia sebagai opsi Default Label pada template Asset Name

8. Buka tab Asset Name pada Settings > Asset Master
9. Ketik Search Asset Name `DU-29`, tekan Enter
10. Klik `[⋯]` pada baris Asset Name `DU-29`, pilih `Edit`
11. Verifikasi Modal Edit Asset Name tampil
12. Klik dropdown Default Label pada Modal Edit Asset Name
13. Verifikasi label `DU-54` tampil sebagai opsi pada dropdown Default Label

### E-FALB-13: Label manual yang ditetapkan sebagai Default Label dipromosikan menjadi default

14. Pilih label `DU-54` pada dropdown Default Label
15. Klik `[Save]`
16. Klik `[Save]` pada dialog Change Default Label
17. Tunggu aksi selesai
18. Ketik Search aset manual `DU-29`, tekan Enter
19. Buka Asset Detail aset manual `DU-29` dari Asset List modul `asset/`
20. Verifikasi chip label `DU-54` tampil pada Asset Detail aset manual `DU-29`
21. Verifikasi ikon `[✕]` tidak tampil pada chip label `DU-54`

### FALB-LOGIC-04f: Promosi provenance mengunci relasi manual yang sudah ada

22. Verifikasi chip label `DU-54` terkunci: ikon `[✕]` tidak tampil pada chip label `DU-54`

### FALB-LOGIC-06c: Cascade retroaktif Default Label bersifat upsert

23. Verifikasi aset manual `DU-29` memiliki tepat satu chip label `DU-54`

### F-FALB-11.k3: Cascade retroaktif mempromosikan relasi manual

24. Verifikasi chip label `DU-54` pada aset manual `DU-29` tidak dapat dilepas lewat ikon `[✕]` karena ikon tidak tampil

## Notes

- Langkah penghubung: langkah 1 dan 18 adalah Search aset target sebelum membuka Asset Detail (R-23); Search `DU-26` pada langkah 1 menyaring kedua aset Active spec dan tetap berisi saat kembali ke Asset List (bagian 8b butir 9); langkah 2, 4, dan 19 membuka Asset Detail dari Asset List modul `asset/`; langkah 8 membuka tab Asset Name; langkah 9 adalah Search untuk menemukan baris target; langkah 10 membuka menu baris; langkah 16 mengonfirmasi dialog dampak Change Default Label; langkah 17 menunggu aksi tulis selesai sebelum berpindah surface.

- Alur dependensi dari PRD `settings-asset-name` (dikutip, dimiliki modul itu; langkah 8 sampai 16 bergantung pada PRD tersebut, bukan pada PRD ini). Kutipan memakai nomor baris file PRD inti `settings-asset-name`:
  - L10: "Tab `Asset Name` di `FAMS > Settings > Asset Master` (sejajar tab "Custom Asset ID" dan "Labels"; bukan menu sidebar terpisah)" dan L324 "Asset Name List | Tab page | Tab `Asset Name`" (langkah 8);
  - L334: "tab `Asset Name`: tabel katalog template aset ... Toolbar, pagination, sort, search, filter, dan download: §5" (langkah 9);
  - L257: "[⋯] > Edit → Modal Edit (§4.1 Popup Create / Edit) → [Save]" dan L394 "Edit | `G-EDIT` ... | Buka Modal Edit"; Total Control ✅ untuk `G-EDIT` (L228) (langkah 10 dan 15);
  - L409: Title `"Edit Asset Name"` (mode Edit) (langkah 11);
  - L418: "`FLD-05` **Default Label (Optional):** Multi-select searchable dropdown yang menampilkan opsi label dengan badge warna aslinya. Placeholder: `"Select default label"`" (langkah 12 sampai 14);
  - L259: "Field berdampak & Total Asset > 0 → dialog dampak ... → konfirmasi → simpan + cascade (FAAM-LOGIC-06)" dan L737 sampai L747 `D-12` "Trigger: Mengubah Default Label pada Asset Name yang memiliki `Total Asset > 0`" dengan tombol "`[Cancel]` dan `[Save]` (primary)" (langkah 16); L780 mengarahkan skenario itu ke `D-09` sampai `D-12`.
  - Kutipan ini dependensi, bukan klausa labeling: tidak ada `Verifikasi` atas isi dialog dampak; langkah 11 adalah anchor positif (S-03) bahwa Modal Edit Asset Name sudah tampil sebelum dropdown Default Label dibuka.
- Anchor absence: chip label tampil pada Asset Detail (langkah 3, 6, 20) mendahului tiap asersi ikon `[✕]` tidak tampil.
- Pembagian klausa lintas spec: `E-FALB-05` dikutip spec 012 dan spec ini; spec ini mengasersi sisi UI (ikon `[✕]` tidak tampil pada relasi default di Asset Detail), spec 012 mengasersi sisi permintaan langsung ke server (penolakan oleh server). Sisi Bulk Remove (`E-FALB-06`, `F-FALB-11.k1`, dan butir Must NOT pelepasan label default) ada di spec 028.
- Dipakai sebagai keadaan yang disyaratkan aturan, tidak diasersi: relasi `default` pada aset default `DU-27` dibuat oleh seeding lewat template Asset Name `DU-27`.
- Temuan PRD: `E-FALB-13` menyatakan "pelepasan berikutnya hanya bisa lewat edit Default Label di Asset Name", klausa yang dimiliki `FALB-LOGIC-04d` yang ditahan; klausa itu tidak diasersi di spec ini.
