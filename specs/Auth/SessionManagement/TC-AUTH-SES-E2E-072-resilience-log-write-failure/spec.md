---
id: TC-AUTH-SES-E2E-072-resilience-log-write-failure
title: "Resilience: Kegagalan Penulisan Log Tidak Membatalkan Log Out"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-216
coverage:
  web: automated
---

# Resilience: Kegagalan Penulisan Log Tidak Membatalkan Log Out

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil BASE (Tabel Data Uji Pre-setup #5: Activated, Active ON, MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-216: `Hendra Setiawan` (`hendrasetiawan+{runId}-072@qwertysystem.net`), Client Alpha Logistik; sesi web Active di Browser A (Chrome on Windows) dibuat BE lewat login nyata
- Konteks (dibuka di hook `before`): Browser A (Chrome on Windows) memuat sesi web seed milik `Hendra Setiawan`.
- State global yang diubah dan dipulihkan: failure injection pada penulisan log (Tabel Data Uji Pre-setup #18). Hook `after` menonaktifkan failure injection walau spec gagal di tengah.
- Suite berjalan serial (`parallel: false`); state global yang diubah: failure injection pada penulisan log, dipulihkan di hook `after`.
- Hook `after`: nonaktifkan failure injection, akhiri sesi seed, tutup konteks Browser A, hapus user seed. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis disediakan tim FE/BE: satu konteks browser dengan user agent yang dapat ditetapkan (Chrome on Windows); failure injection pada penulisan log di sisi server (Tabel Data Uji Pre-setup #18); pembacaan status sesi user uji dari sisi backend (langkah 3, prakondisi d TC-AUTH-SES-216), disediakan tim FE/BE, tanpa endpoint; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: `Hendra Setiawan` pada Browser A.

## Test Steps

### TC-AUTH-SES-216: Kegagalan penulisan log tidak membatalkan Log Out (log pasca-commit, best-effort)

1. Aktifkan failure injection pada penulisan log
2. Di Browser A (sesi web Active `Hendra Setiawan`, Chrome on Windows) klik menu Profile lalu pilih Log Out
3. Baca status sesi `Hendra Setiawan` dari BE uji
4. Verifikasi Logout tetap berhasil: sesi berstatus Logged Out
5. Verifikasi Browser A diarahkan ke halaman Login with Password
6. Verifikasi Tidak ada toast error
7. Nonaktifkan failure injection pada penulisan log

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: fault injection pada penulisan log (kelas b); `Mode: FE+BE` karena failure injection di sisi server. TC-AUTH-SES-216 ada di spec ini; spec `TC-AUTH-SES-E2E-061` memuat TC struktur dan format surface log lainnya.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): mengaktifkan dan menonaktifkan failure injection (langkah 1 dan 7; hook `after` sebagai cadangan, S-09); klik Log Out; membaca status sesi dari BE uji (langkah 3).
- Temuan untuk QA: TC-AUTH-SES-216 Expected butir c ("dapat tertunda atau tidak tertulis") nondeterministik; spec hanya mengasersi hasil Log Out tidak berubah (langkah 4 sampai 6) dan tidak mengasersi ada atau tidaknya entri `Logged out`. Prakondisi d TC-AUTH-SES-216 menyebut status sesi dapat dibaca dari BE uji tanpa menyebut mekanisme; spec mengandalkan kemampuan pembacaan status sesi di Prerequisites tanpa menyebut endpoint.
