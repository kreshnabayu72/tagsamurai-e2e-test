# Coverage E2E — Auth > Account Activation

Sumber: `auth/account-activation/TestCases/tc-account-activation.md` (134 TC aktif, diperbarui 2026-10-07, tanpa celah nomor). Suite: `specs_dummy/Auth/AccountActivation/`. Status semua spec: `draft`, belum ada script.

**Verifikasi lint:** `npx spectra lint --strict specs_dummy/Auth/AccountActivation` → `✓ 28 specs and 1 suites verified. 0 lint errors found.`

**Aturan seleksi:** sesuai `docs/e2e-conventions.md` bagian 2, spec e2e merangkap TC FE. Semua 134 TC FE masuk spec (tidak ada hanya-BE di namespace FE; TC hanya-BE ada di `tc-account-activation-backend.md` dan tidak dipetakan ke spec ini, lihat bagian 8). Spec yang butuh kondisi terpicu (intercept untuk error/timeout/rate limit, fixture waktu, fixture status/kredensial, mailbox, dua sesi browser) mencatat kebutuhannya di `Prerequisites`. Hambatan teknis, termasuk label "Manual Only" di TC, tidak menjadi alasan mengeluarkan TC.

**Nomor folder.** Prefix `TC-AUTH-ACT-E2E-` berasal dari `AUTH` + `ACT` (Account Activation). Nomor adalah urutan spec (`001`–`028`), bukan nomor TC sumber. Setelah regenerasi 2026-10-08 dari TC canonical 134, penomoran dilakukan ulang dari nol: **spec lama (21 spec, TC 94) tidak dipetakan ke id baru** dan tidak ada pemetaan id TC legacy ke id TC granular yang baru. Spec lama di `specs/Auth/AccountActivation/` dibiarkan apa adanya dan sudah basi (sumbernya TC 94); kanonisasi ke `specs/` beserta promosi `status` dijadwalkan terpisah setelah review.

**Verifikasi duplikasi:** 134 TC granular terreferensi tepat 1 spec, 0 duplikasi, 0 tidak terpetakan (dicek dengan skrip: `sourceTc` tiap spec dibaca, id `TC-AUTH-ACT-01`–`134` harus muncul tepat 1×). Nama folder setiap spec sama persis dengan `id` di frontmatter `spec.md` (dicek skrip yang sama; lolos).

## TC granular → spec e2e

| Spec | Isi | TC sumber | Platform |
|---|---|---|---|
| TC-AUTH-ACT-E2E-001 | Screening link entry: Set Password tampil, judul/subtitle tombol, token di URL | 1, 7, 8, 10 | web |
| TC-AUTH-ACT-E2E-002 | Validasi link saat dibuka: loading, error state [Try Again], token tidak dikenal/kosong/429 rate limit | 2–6, 133 | web |
| TC-AUTH-ACT-E2E-003 | Trigger Activation Email dari Global Settings > User: hasilkan token, kirim email, kegagalan kirim | 11, 13–16 | web |
| TC-AUTH-ACT-E2E-004 | Trigger Activation Email dari Admin Console | 12 | web |
| TC-AUTH-ACT-E2E-005 | Kegagalan kirim email dan pemulihan via Resend | 17, 18 | web |
| TC-AUTH-ACT-E2E-006 | Password Policy & checklist real-time (per baris aturan, per keystroke) | 22–29 | web |
| TC-AUTH-ACT-E2E-007 | Toggle show/hide independen per field + ikon dan tooltip sesuai state | 19–21 | web |
| TC-AUTH-ACT-E2E-008 | Boundary panjang 72/73/80 karakter dan karakter khusus pada checklist | 30–36 | web |
| TC-AUTH-ACT-E2E-009 | Validasi submit: field kosong, urutan evaluasi, Confirm tidak sama | 38–44, 53–56 | web |
| TC-AUTH-ACT-E2E-010 | Submit diblokir client karena policy + ketiadaan CAPTCHA | 37, 45–52, 57 | web |
| TC-AUTH-ACT-E2E-011 | Guard halaman Set Password (tanpa dialog Unsaved Changes) dan accessibility | 58–62 | web |
| TC-AUTH-ACT-E2E-012 | Happy path aktivasi, boundary password valid, loading, klik ganda | 63–65, 70, 71 | web |
| TC-AUTH-ACT-E2E-013 | Kegagalan server Set Password (5xx, timeout, 429) dan retry sukses | 66–69, 134 | web |
| TC-AUTH-ACT-E2E-014 | Activation Success, CTA Go to Login, guard akses halaman sukses | 73–78 | web |
| TC-AUTH-ACT-E2E-015 | Invalid Link: token tidak dikenal/kosong/terpotong dan varian Used | 9, 79–84 | web |
| TC-AUTH-ACT-E2E-016 | Boundary masa berlaku token: 23j59 valid, 25 jam expired | 86, 87 | web |
| TC-AUTH-ACT-E2E-017 | Link milik user yang dihapus (saat dibuka dan saat form terbuka) | 88, 125 | web |
| TC-AUTH-ACT-E2E-018 | Pengaruh toggle Active OFF terhadap link dan aktivasi | 72, 89, 126 | web |
| TC-AUTH-ACT-E2E-019 | Zero-logging lintas aksi di 4 surface log | 90–97 | web |
| TC-AUTH-ACT-E2E-020 | Cross-module: gate login, refleksi status Activated, siklus toggle | 98, 106–109 | web |
| TC-AUTH-ACT-E2E-021 | Resend dari Global Settings > User: invalidasi, status, masa berlaku token baru | 85, 99, 102–105 | web |
| TC-AUTH-ACT-E2E-022 | Resend dari Admin Console dan Bulk Resend | 100, 101 | web |
| TC-AUTH-ACT-E2E-023 | Kondisi Client (Suspended/Expired) dan plan (Starter/Enterprise) | 110–112 | web |
| TC-AUTH-ACT-E2E-024 | Token scope dan injeksi token (SQL/skrip) | 113, 119, 120 | web |
| TC-AUTH-ACT-E2E-025 | Enforcement server: request langsung password/Confirm tidak valid → 422 | 114–116, 128 | web |
| TC-AUTH-ACT-E2E-026 | Tampilan respons 422 dengan field, 400 tanpa field, 400 tanpa token | 117, 118, 132 | web |
| TC-AUTH-ACT-E2E-027 | Race dua tab, submit kedua, dan submit token tidak dikenal → 404 | 121, 122, 127, 131 | web |
| TC-AUTH-ACT-E2E-028 | Perubahan state saat form terbuka (Resend, expired, status, password ada) | 123, 124, 129, 130 | web |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| 1, 7, 8, 10 | TC-AUTH-ACT-E2E-001 | FE+BE |
| 2–6, 133 | TC-AUTH-ACT-E2E-002 | mock |
| 11, 13–16 | TC-AUTH-ACT-E2E-003 | FE+BE |
| 12 | TC-AUTH-ACT-E2E-004 | FE+BE |
| 17, 18 | TC-AUTH-ACT-E2E-005 | FE+BE |
| 22–29 | TC-AUTH-ACT-E2E-006 | FE+BE |
| 19–21 | TC-AUTH-ACT-E2E-007 | FE+BE |
| 30–36 | TC-AUTH-ACT-E2E-008 | FE+BE |
| 38–44, 53–56 | TC-AUTH-ACT-E2E-009 | FE+BE |
| 37, 45–52, 57 | TC-AUTH-ACT-E2E-010 | FE+BE |
| 58–62 | TC-AUTH-ACT-E2E-011 | FE+BE |
| 63–65, 70, 71 | TC-AUTH-ACT-E2E-012 | mock |
| 66–69, 134 | TC-AUTH-ACT-E2E-013 | mock |
| 73–78 | TC-AUTH-ACT-E2E-014 | FE+BE |
| 9, 79–84 | TC-AUTH-ACT-E2E-015 | FE+BE |
| 86, 87 | TC-AUTH-ACT-E2E-016 | mock |
| 88, 125 | TC-AUTH-ACT-E2E-017 | FE+BE |
| 72, 89, 126 | TC-AUTH-ACT-E2E-018 | FE+BE |
| 90–97 | TC-AUTH-ACT-E2E-019 | FE+BE |
| 98, 106–109 | TC-AUTH-ACT-E2E-020 | FE+BE |
| 85, 99, 102–105 | TC-AUTH-ACT-E2E-021 | FE+BE |
| 100, 101 | TC-AUTH-ACT-E2E-022 | FE+BE |
| 110–112 | TC-AUTH-ACT-E2E-023 | FE+BE |
| 113, 119, 120 | TC-AUTH-ACT-E2E-024 | FE+BE |
| 114–116, 128 | TC-AUTH-ACT-E2E-025 | FE+BE |
| 117, 118, 132 | TC-AUTH-ACT-E2E-026 | mock |
| 121, 122, 127, 131 | TC-AUTH-ACT-E2E-027 | FE+BE |
| 123, 124, 129, 130 | TC-AUTH-ACT-E2E-028 | mock |

Kolom Mode mengikuti penanda `Mode: mock` di `Prerequisites` spec (intercept respons, fixture waktu/kecepatan, atau fixture BE); sisanya `FE+BE`. Kolom BE dicatat pada tingkat endpoint karena `tc-account-activation-backend.md` tidak merujuk id TC granular.

## Catatan regenerasi 2026-10-08

Regenerasi menggantikan seluruh 21 spec lama (dibuat dari TC 94) dengan 28 spec baru (dari TC 134). Pengelompokan disusun ulang mengikuti `docs/e2e-conventions.md`: satu spec = satu sesi dengan topik/dataset/kebutuhan teknis yang sama, aksi destruktif (aktivasi sukses, pengonsumsian token) di akhir spec. Tidak ada pemetaan 1:1 dari spec lama ke spec baru, sehingga tabel pemetaan split tidak dipertahankan; lacak perubahan lewat git history file `specs_dummy/Auth/AccountActivation/` dan tabel TC granular → spec di atas.

## TC belum dipetakan

Tidak ada TC FE yang belum dipetakan: 134/134 masuk spec (verifikasi otomatis). TC hanya-BE berada di `auth/account-activation/TestCases/tc-account-activation-backend.md` dan sengaja tidak dipetakan ke spec e2e web; endpoint-nya dicatat pada tingkat suite di `tc-account-activation-backend.md`.
