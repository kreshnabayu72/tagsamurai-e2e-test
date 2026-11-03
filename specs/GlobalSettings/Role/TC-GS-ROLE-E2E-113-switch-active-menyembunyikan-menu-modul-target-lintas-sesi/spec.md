---
id: TC-GS-ROLE-E2E-113-switch-active-menyembunyikan-menu-modul-target-lintas-sesi
title: "Switch Active OFF Menyembunyikan Menu Modul Target pada Sesi User Target, ON Menampilkannya Kembali"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-331
coverage:
  web: automated
---

# Switch Active OFF Menyembunyikan Menu Modul Target pada Sesi User Target, ON Menampilkannya Kembali

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua sesi UI), kelas c; Sesi B adalah objek asersi sidebar. Suite `parallel: false` karena spec mengubah baris role user Pre-setup bersama.
- Akun Sesi A (UI): Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Password tidak ditulis di spec atau fixture.
- Akun Sesi B (UI): Hanif Pradipta (Pre-setup #20: Active, baris `Manage TAG` Active dengan Read dan Update tercentang, Access Global Settings dicentang). Email dan kredensial disediakan tim FE (Tabel Pre-setup TC tidak memuat email; lihat Temuan untuk QA). Konteks browser kedua ini dibuka dan login di hook `before` spec ini (sidebar menampilkan menu TAG sesuai precondition TC) dan ditutup di hook `after`.
- Kemampuan teknis: dua konteks browser paralel (Sesi A dan Sesi B); langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`. Nilai identitas user mengacu fixture `Fixture.role.*` yang dibuat di tahap script (berkas belum ada).
- Given (hook `before`): `Hanif Pradipta` dipastikan berada di state di atas. Mekanisme menyiapkan baris role Active per user disediakan tim FE/BE; endpoint Switch Active tidak didefinisikan di TC, PRD, atau LLD (lihat Temuan untuk QA).
- Pemulihan (hook `after`, tidak berasumsi aksi berhasil penuh): baris `Manage TAG` `Hanif Pradipta` dikembalikan Active dengan Read dan Update tercentang; konteks Sesi B ditutup; sesi dipulihkan ke akun default suite. Efek pada Pre-setup: Modified By dan Last Updated berubah; entri log bersifat immutable dan tidak dihapus.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite) untuk akun UI yang dipakai suite, termasuk akun target; spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada selain data Given di atas.

## Test Steps

### TC-GS-ROLE-331: Switch Active OFF menyembunyikan menu modul target pada request berikutnya dan ON menampilkannya kembali

1. [Sesi B] Verifikasi menu TAG tampil di sidebar `Hanif Pradipta`
2. [Sesi A] Buka Global Settings > User > User List (sub-tab Login User), ketik Search `Hanif Pradipta`, tekan Enter
3. [Sesi A] Klik Name `Hanif Pradipta`, buka Tab `Role`
4. [Sesi A] Matikan switch `Manage TAG`
5. [Sesi A] Tunggu aksi selesai
6. [Sesi B] Reload halaman
7. [Sesi B] Verifikasi area konten Global Settings tampil
8. [Sesi B] Verifikasi menu TAG tidak tampil di sidebar `Hanif Pradipta`
9. [Sesi A] Nyalakan switch `Manage TAG`
10. [Sesi A] Tunggu aksi selesai
11. [Sesi B] Reload halaman
12. [Sesi B] Verifikasi menu TAG tampil kembali di sidebar `Hanif Pradipta`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua sesi UI), prinsip 13c bagian 3 konvensi; Sesi B bukan pemicu melainkan objek asersi sidebar, sehingga tidak memakai butir `P-2`. Satu TC sumber.
- Langkah 1 (menu TAG tampil) adalah precondition TC-331 (butir b: "sidebar menampilkan menu TAG") dan bukan Expected; dipakai sebagai anchor positif bahwa sidebar Sesi B terbaca sebelum asersi absence pada langkah 8.
- Langkah 7 (area konten Global Settings tampil sesudah reload) adalah anchor positif untuk absence menu TAG pada langkah 8 (bagian 8b butir 2 dan R-21): sidebar `Hanif Pradipta` tidak punya item menu lain karena baris `Manage TAG` adalah satu-satunya role.
- Search untuk menemukan user target ditulis sebagai langkah penghubung (R-16): langkah 2. Langkah penghubung lain (aksi tanpa `Verifikasi`): membuka Tab `Role` (langkah 3), "Tunggu aksi selesai" (langkah 5 dan 10), dan reload Sesi B (langkah 6 dan 11).
- Temuan untuk QA:
  - Email dan kredensial akun `Hanif Pradipta` (login sendiri) tidak ada di Tabel Pre-setup TC; ditulis "disediakan tim FE".
  - Mekanisme menyiapkan baris role Active per user (Pre-setup #20) tidak ada di TC, PRD, atau LLD; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
  - TC-GS-ROLE-331 bertanda `Manual Only (d)` karena dua sesi paralel; spec tetap memuatnya (hambatan teknis bukan alasan mengeluarkan TC).
  - Sidebar `Hanif Pradipta` hanya memuat menu TAG sehingga tidak ada item menu lain sebagai anchor absence pada sidebar yang sama; spec memakai area konten halaman sebagai anchor.
