---
name: Auth Login with Password
id: suite-auth-login-password
description: Test cases derived from tc-login-password.md for Auth > Login with Password
executionOrder: 1.0
parallel: false
---

# Suite: Auth Login with Password

Suite ini mencakup alur Login with Password secara penuh: screening halaman login, validasi field Email dan Password, Google reCAPTCHA v2 gate (web), penolakan status akun (Pending Activation, Inactive / Toggle Global OFF) dan email belum terdaftar, login berhasil ke Portal tanpa gate lintas 5 paket tier plan, lock progression bertahap (15 menit, 1 jam, Requires Reset, dan eskalasi 7 hari berturut-turut menjadi Permanent), pemulihan lock via Reset Password dan reset counter harian oleh login berhasil, Agreement gate (Confirm to Continue) dengan tiga kondisi pemicu beserta siklus persetujuan dan lifecycle token pre-auth, konsumsi persetujuan Privacy Policy lintas modul (Login with OTP dan Biometric Re-login), handoff ke layar MFA untuk device baru dan anomali lokasi geografis, navigasi ke Login with OTP dan Reset Password dengan prefilled email, resilience & loading state saat kegagalan server (500, timeout), pembatasan laju request per IP (20 req/menit), pencatatan audit log di dua surface (Activity Log > Session dan User Log) untuk status sukses maupun gagal serta verifikasi kondisi yang tidak dicatat, sinkronisasi realtime perubahan status akun dari Global Settings > User, concurrency & race condition submit kredensial salah, layout mobile app tanpa reCAPTCHA, serta independensi lock akun antar platform web dan mobile.

`parallel: false` karena beberapa alasan berikut:

- IP Rate Limiting (E2E-015) membatasi maksimal 20 request per menit per alamat IP; request dari spec lain yang berjalan bersamaan dari IP yang sama akan memicu blokir 429 dan merusak hasil uji spec lainnya.
- Spec lock progression (E2E-006, E2E-007, E2E-008) memanipulasi counter kegagalan (`failed_count`), tahap lock (`lock_level`), batas waktu lock (`lock_until`), dan riwayat hari berturut-turut (`consecutive_1h_days`) pada user tertentu di backend/database.
- Spec audit log (E2E-016, E2E-017, E2E-018) memverifikasi delta jumlah baris dan urutan entri di Activity Log > Session dan User Log; eksekusi paralel akan mencemari baris log dan menyebabkan asersi jumlah entri meleset.
- Spec sinkronisasi lintas modul (E2E-019) memodifikasi Toggle Global dan status hapus user di Global Settings > User secara live.
- Concurrency dan race condition (E2E-020) menguji persaingan submit multi-tab untuk akun yang sama sehingga membutuhkan environment yang terisolasi dari intervensi run lain.

Setiap spec menyiapkan data ujinya sendiri melalui hook `before`/`beforeEach` dan membersihkannya pada `after`/`afterEach`.
