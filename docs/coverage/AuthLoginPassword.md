# Coverage E2E — Auth > Login with Password

Sumber: `auth/login-password/TestCases/tc-login-password.md` (74 TC aktif). Suite: `specs/auth2/LoginPassword/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `npx spectra lint --strict specs/auth2/LoginPassword` → `✓ 20 specs and 1 suites verified. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, spec e2e merangkap TC FE. Semua TC masuk spec kecuali hanya-BE. Spec yang butuh kondisi terpicu(created via API, intercept, atau viewport mobile) ditandai `Mode: mock`. Hambatan teknis dicatat di `Prerequisites`, bukan menjadi alasan mengeluarkan TC.

**Nomor folder.** Prefix `TC-AUTH-LP-E2E-` berasal dari `AUTH` + `LP` di `foundation/tc-prefix-registry.md`. Nomor adalah urutan spec, bukan nomor TC sumber, sehingga tidak sama dengan nomor TC granular.

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-LP-E2E-001 | Screening halaman login, validasi Email dan Password, batas 120 karakter, show/hide password | 1, 4, 5, 6, 7, 9, 11, 12, 13, 93 | web |
| TC-AUTH-LP-E2E-002 | Login berhasil tanpa trigger Agreement maupun MFA: email di-trim, email 120 karakter, lintas plan dan entity, handoff Session Management | 8, 10, 47, 51, 88, 89 | web |
| TC-AUTH-LP-E2E-003 | Pencatatan login sukses di kedua surface, kolom IP Address, format Device / Browser, attempt tanpa subjek tidak dicatat | 55, 57, 59, 94 | web |
| TC-AUTH-LP-E2E-004 | Percobaan salah pertama dan kedua tanpa lock, plus pencatatan di kedua surface | 31, 32, 56, 64 | web |
| TC-AUTH-LP-E2E-005 | Lock 15 menit pada percobaan ketiga, submit selama window aktif, lock yang sudah lewat, akumulasi counter lintas tab | 33, 34, 35, 92 | web |
| TC-AUTH-LP-E2E-006 | Lock 1 jam, status requires reset, dan submit selama tiap window aktif | 36, 37, 38 | web |
| TC-AUTH-LP-E2E-007 | Pergantian hari mereset tahap 15 menit dan 1 jam, status yang tidak direset, eskalasi tujuh hari, rantai yang terputus | 39, 40, 41, 42, 43 | web |
| TC-AUTH-LP-E2E-008 | Reset Password yang berhasil melepas seluruh tahap lock dan counter consecutive | 44, 87 | web |
| TC-AUTH-LP-E2E-009 | CAPTCHA gate web: submit tanpa token, submit dengan token, token sekali pakai, urutan CAPTCHA sebelum status akun | 15, 16, 30 | web |
| TC-AUTH-LP-E2E-010 | Provider reCAPTCHA timeout diperlakukan sebagai kegagalan server | 18 | web (`Mode: mock`) |
| TC-AUTH-LP-E2E-011 | Account status gate: belum aktivasi, inactive, baru dinonaktifkan, dihapus, baru diaktivasi | 28, 29, 85, 86, 91 | web |
| TC-AUTH-LP-E2E-012 | Agreement gate: tiga kondisi pemicu, aksi tanpa centang, centang lalu lanjut, dan kondisi tidak-terpicu | 19, 20, 21, 22, 23, 24, 90 | web |
| TC-AUTH-LP-E2E-013 | Penutupan layar Confirm to Continue dan preAuthToken kedaluwarsa | 25, 26 | web |
| TC-AUTH-LP-E2E-014 | Handoff ke MFA, pre-auth web tanpa device, dan pre-auth unauthorized | 48, 49, 50 | web |
| TC-AUTH-LP-E2E-015 | Navigasi keluar halaman login, email handoff ke OTP dan Reset Password, email prefilled dari Edit email | 3, 52, 53, 54 | web |
| TC-AUTH-LP-E2E-016 | Double-submit, retry setelah client timeout, dan rate limit per IP | 60, 61, 63 | web |
| TC-AUTH-LP-E2E-017 | Kegagalan server saat submit dan tidak adanya asumsi sukses sebelum konfirmasi server | 62, 68 | web (`Mode: mock`) |
| TC-AUTH-LP-E2E-018 | Aksesibilitas: urutan fokus keyboard, asosiasi caption error, pengumuman caption lock | 79, 80, 81 | web (`Mode: mock`) |
| TC-AUTH-LP-E2E-019 | Mobile app: layout layar penuh tanpa reCAPTCHA, submit tanpa token CAPTCHA | 2, 17 | **mobile** |
| TC-AUTH-LP-E2E-020 | Lock per-platform independen: user terkunci di web tetap bisa login di mobile | 45 | **mobile** |

Total: 74 dari 74 TC aktif tercakup, tanpa duplikasi. 18 spec web, 2 spec mobile.

## TC sumber yang tidak masuk spec

TC berikut tidak lagi ada di file TC aktif, jadi tidak punya spec. Numbers di bawah adalah celah yang disengaja dan tidak diurutkan ulang.

| TC | Alasan |
|---|---|
| 14, 27, 46, 58, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78 | Changelog 2026-09-04: 17 TC murni API Backend dihapus |
| 82, 83, 84 | Changelog 2026-10-01: 3 TC layout mobile/responsive dicabut, file TC dinyatakan web-only |

## Verifikasi silang

- Tidak ada `sourceTc` yang muncul di dua spec. Script audit terhadap `sourceTc` seluruh spec melaporkan `DUPLICATE: none`.
- Nomor langkah tiap spec dimulai dari 1 dan berurutan tanpa lompatan.
- Semua judul berformat `... : ...` sudah diapit tanda kutip agar frontmatter YAML valid.

## Hasil audit silang terhadap `tc-login-password-frontend.md`

`tc-login-password-frontend.md` berisi 44 case FE yang merujuk 69 TC granular. Audit dua arah dilakukan terhadap file tersebut.

### Arah TC di file FE → spec: tidak ada yang terlewat

Seluruh 69 TC yang dirujuk `tc-login-password-frontend.md` sudah ada di `sourceTc` spec. Tidak ada satu pun TC FE yang hilang.

### Arah spec → file FE: 5 TC tidak dirujuk file FE

| TC | Sifat di `tc-login-password.md` | Alasan tidak ada di file FE | Spec mana yang memuat |
|---|---|---|---|
| `TC-AUTH-LP-63` | `Manual Only` | Di-exclude Aturan #5 file FE karena berlabel `Manual Only` | 016 |
| `TC-AUTH-LP-88` | `Manual Only` | Di-exclude Aturan #5 file FE karena berlabel `Manual Only` | 002 |
| `TC-AUTH-LP-92` | Automatable | Ditambahkan setelah snapshot file FE | 005 |
| `TC-AUTH-LP-93` | Automatable | Ditambahkan setelah snapshot file FE | 001 |
| `TC-AUTH-LP-94` | Automatable | Ditambahkan setelah snapshot file FE | 003 |

Kelima TC tetap masuk spec atas keputusan eksplisit: label `Manual Only` bukan alasan mengeluarkan TC menurut `docs/e2e-conventions.md` bagian 2, dan `92` sampai `94` memang `Automatable` sehingga baru ditambahkan. Header file FE masih menyebut cakupan sampai `TC-AUTH-LP-91`. Detailnya tercatat sebagai `GAP-LP-E2E-007`.

### Perbaikan hasil audit expected-result

Audit ini menemukan 8 ketidaksesuaian isi antara file FE, `tc-login-password.md`, dan PRD. Semuanya sudah dikoreksi di spec:

| # | Spec | TC | Koreksi |
|---|---|---|---|
| 1 | 013 | `25` | Tutup layar sekarang menguji entri `Failed` + Note `Consent not given` sesuai PRD §9.2 dan §11.4, bukan "jumlah entri tidak berubah" |
| 2 | 013 | `26` | Token kedaluwarsa sekarang menguji status `422` dengan kode `TOKEN_EXPIRED` dan redirect ke halaman Login penuh |
| 3 | 005 | `33` | Ditambahkan assert Note `Locked 15 minutes` beserta `lock_level` dan `lock_until` |
| 4 | 006 | `36` | Ditambahkan assert Note `Locked 1 hour` beserta `lock_level`, `lock_until`, dan `consecutive_1h_days` |
| 5 | 001 | `11` | Ditambahkan assert Note `Empty password` pada kedua surface log |
| 6 | 001 | `12` | Ditambahkan assert Note `Incorrect password` dan kenaikan `failed_count` |
| 7 | 006 | — | Prerequisites ditulis ulang agar `wrongPasswords` Indexed 0 sampai 6 tercatat eksplisit beserta pembagiannya per user |
| 8 | 006, 013 | — | Teks parameter kosong dibersihkan, termasuk catatan `Jed-request` yang sebelumnya rusak |

Spec 001 juga dirombak: sebelumnya Email kosong dan Password kosong diuji dalam satu submit, padahal `TC-AUTH-LP-5` mensyaratkan Password terisi untuk Email kosong, sedangkan `TC-AUTH-LP-11` mensyaratkan Email valid dan terdaftar untuk Password kosong. Satu submit tidak bisa memenuhi kedua prasyarat itu sekaligus, jadi keduanya dipisah.

## Pola steady-state yang dipakai

Setiap spec mengikuti pola berikut supaya dapat dijalankan sendiri:

1. **Prerequisites** memuat hook yang menyiapkan state: user dibuat lewat API Global Settings > User dengan `failed_count`, `lock_level`, `lock_until`, dan `consecutive_1h_days` tertentu, lalu dikembalikan ke awal di `afterEach`.
2. **Verifikasi state** selalu dibaca dari Global Settings > User > User Log atau dari Global Settings > Activity Log > Session, bukan dari banner dan bukan dari asumsi jumlah submit. Banner hanya menampilkan tahap lock dan waktu absolut, bukan counter.
3. **Pembersihan** ditulis sebagai logout pada langkah di dalam spec atau sebagai hook `afterEach`, tidak pernah bergantung pada logout di spec sebelumnya.
4. **Kebutuhan environment** yang belum tersedia (mailbox uji, pemicu waktu, pre-auth token, pemicu pergantian hari, TTL token pendek, device) dicatat di Prerequisites sebagai sumber resmi bagi tim FE.
5. **Tidak ada nilai sensitif** yang ditulis di spec maupun fixture. Password lewat `Spectra.env.AUTH_PASSWORD` dan `Spectra.env.AUTH_PASSWORD_2`.

## Keputusan yang perlu ditinjau

- `parallel: false` pada suite, karena lima spec saling memengaruhi: rate limit per IP, state lock yang dibuat lewat API, dan spec yang butuh state awal sudah terkunci.
- `TC-AUTH-LP-88` berstatus `Manual Only` di TC granular. Sesuai e2e-conventions.md bagian 2 label tersebut bukan alasan mengeluarkan TC, dan spec 002 hanya menguji handoff-nya. Perilaku Duplicate Login Attempt sendiri milik modul `session-management`.
- `TC-AUTH-LP-63` masih `[TODO Engineering]` untuk threshold. Spec 016 menjalankan request berulang sampai 429 muncul dan mencatat jumlah request-nya sebagai bahan konfirmasi threshold, bukan mengasumsikan angka final.
- Spec 019 dan 020 memakai `coverage.mobile`, sesuai aturan bahwa TC mobile tetap diotomasikan meski file TC menyatakan web-only. Ketiga TC mobile yang tersisa adalah 2, 17, dan 45.