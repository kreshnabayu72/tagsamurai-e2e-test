---
id: TC-GS-DIV-E2E-034-delete-katalog-terakhir-otomatis-in-use
title: "Delete Division: Katalog Tidak Pernah Turun ke Nol"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-279
coverage:
  web: automated
---

# Delete Division: Katalog Tidak Pernah Turun ke Nol

## Prerequisites

- Mode: FE+BE. Kelas harness: blokir karena kondisi data (prinsip 12; entitas dengan tepat satu Division). Spec tidak mengubah atau menghapus data.
- Akun aktor: Total Control pada entitas khusus yang hanya punya 1 Division yang dipakai Default User entitas. Email dan kredensial akun tidak ada di Tabel Data Uji Pre-setup Division; disediakan tim FE. Nama env var password diusulkan `GS_ONEDIV_TC_PASSWORD` (tim FE menetapkan dan mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_ONEDIV_TC_PASSWORD` (usulan) dan `GS_TC_PASSWORD` (pemulihan sesi di hook `after`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup entitas khusus (tetap di environment): tepat 1 Division dengan nama tetap, dipakai Default User entitas. Fixture belum ada; tim FE menyiapkan kunci `soleDivision` (nama Division tunggal) pada fixture Division.
- Data dinamis: tidak ada; tidak ada seeding dan tidak ada cleanup selain membersihkan seleksi. Hook `beforeEach`: tutup dialog yang terbuka lalu kembali ke Global Settings > User > Division.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-279: Katalog tidak pernah turun ke nol, Division terakhir otomatis in-use

1. Centang satu-satunya baris Division
2. Klik `Bulk Action` > `Delete`
3. Verifikasi dialog `Cannot Delete Data` tampil
4. Verifikasi dialog memuat bullet nama Division tunggal entitas (`soleDivision`)
5. Verifikasi dialog memuat tombol `[OK]`
6. Klik `[OK]`
7. Verifikasi Division tunggal entitas tetap ada di tabel
8. Verifikasi tabel tidak menampilkan empty state (katalog tidak turun ke 0)
9. Klik icon `(✕)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Langkah penghubung (aksi tanpa `Verifikasi`): 6 (klik `[OK]` untuk menutup dialog; TC sumber tidak menyebutnya), 9 (membersihkan seleksi).
- Entitas dengan tepat satu Division tidak dapat dibentuk di entitas utama suite karena Division Pre-setup `Human Resources`, `Operations`, dan `Compliance` in-use dan tidak dapat dihapus; karena itu TC memakai entitas khusus.
- Temuan untuk QA:
  - TC-279 precondition ("Hanya 1 Division tersisa dan dipakai oleh Default User entitas") tidak menyebut entitas atau akun yang memenuhinya dan tidak ada di Tabel Data Uji Pre-setup. Spec memakai entitas khusus yang disediakan tim FE (akun, email, dan nama env var belum ada).
  - TC-279 Post Condition ("Jumlah Division tetap 1") punya padanan di butir b (Division tetap ada); asersi memakai baris tetap ada dan empty state tidak tampil.
  - Akun entitas khusus tidak ada di daftar akun aktor suite; penyetelan flag Guided Tooltip untuk akun ini oleh hook suite disediakan tim FE.
  - TC-279 butir a menyebut bullet `[nama Division]` tanpa nilai; spec memakai nama dari fixture `soleDivision`.
