# Usulan Naik ke "Di Dalam Filter": Global Settings > My Profile

Modul: Global Settings > My Profile (Change Password, Edit Photo, Pending Email Change, Storage, Sinkron Data Admin, Plan)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/MyProfile`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

Semua spek di modul ini berstatus "Belum ada skrip", jadi kolom status tidak membedakan. Penilaian sepenuhnya dari dampak bisnis dan keamanan akun.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-030 | Change Password: Batas Waktu Boleh-Coba-Lagi (Satu Langkah Sebelum, Tepat, dan Setelah) | High | Batas percobaan ganti password yang salah membuka celah tebak password | Belum ada skrip | tidak |
| E2E-032 | Change Password: Reset Hitungan Harian per Timezone, Lock Melewati Tengah Malam, dan Eskalasi 7 Hari | High | Hitungan percobaan dan eskalasi lock yang salah membuat akun terbuka untuk tebakan berulang, atau terkunci tanpa alasan | Belum ada skrip | tidak |
| E2E-048 | Pending Email Change: Tautan Konfirmasi Kurang dari 24 Jam, Lebih dari 24 Jam, dan Halaman 404 Confirmation Link Expired | High | Tautan konfirmasi yang kedaluwarsa masih bisa dipakai untuk mengubah email akun | Belum ada skrip | tidak |
| E2E-056 | Sinkron Data Admin: Rename Position dan Division, Pair dan Unpair TAG, Reset Authenticator | Medium | Reset Authenticator oleh admin mengubah kredensial MFA user. Yang lain berupa tampilan sinkron | Belum ada skrip | tidak |
| E2E-060 | Storage di Bawah Kuota, Tanpa Kuota, Cek Ledger, dan Perubahan Kuota di License Allocation | High | Edit Photo yang melewati kuota storage tidak diblokir, dan ledger yang salah membuat kuota tidak akurat | Belum ada skrip | tidak |
| E2E-068 | State Tenant: Plan Starter dan Enterprise Tanpa Gating pada Change Password dan Edit Photo | Medium | Plan yang salah membatasi Change Password atau Edit Photo di satu tier | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- E2E-063 (Multi-Tab: Edit Photo dan Delete Photo bersamaan): last-write-wins pada foto profil, dampak kecil dibanding keamanan akun dan kuota.
- E2E-007 (Guided Tooltip): tampilan, dampak rendah.
- E2E-027 (guard refresh browser dan pindah menu saat modal terisi): kehilangan isian form, dampak sedang, dan tidak berkaitan dengan data atau akses.

## Catatan untuk FE/QA

- E2E-030, E2E-032, dan E2E-048 membutuhkan pengaturan waktu server dan browser (jam tiruan). Mekanismenya belum didefinisikan di TC, jadi ditulis sebagai kemampuan tim FE/BE.
- E2E-032 membutuhkan dua zona waktu, satu untuk user dan satu untuk UTC. Akun pembaca User Log juga belum disebut di TC.
- E2E-060 membutuhkan ledger storage yang bisa diatur. Perubahan kuota lewat License Allocation juga membutuhkan akun pelaku yang disediakan tim FE.
- E2E-056 mengubah kredensial MFA akun uji. Spec memulihkan enrollment-nya sendiri, dan ini perlu dicek QA.
- Daftar ini hanya mencakup 9 spek yang diajukan untuk My Profile. Semua spek di sini belum punya skrip.
