---
name: tagsamurai-e2e-generate-script
description: Workflow untuk menulis web.test.ts, Page Object, Step, hook, dan fixture dari spec.md e2e TAG Samurai yang sudah disetujui. Dipakai setelah spec.md berstatus ready-for-automation.
---

# Generate Script E2E dari spec.md

Aturan lengkap ada di `docs/e2e-conventions.md`. Skill framework yang wajib dipatuhi: `page-objects-and-selectors`, `shared-steps-and-actions`, `lifecycle-hooks`, `fixtures-data`, `matchers-and-assertions`, `network-interception`, `spec-and-suite-authoring`.

## Input yang wajib ada

- Path suite atau spec yang sudah `ready-for-automation`. Spec berstatus `draft` tidak dikerjakan.
- Untuk elemen UI, selector yang tersedia di app (`aria-label` atau `data-testid`). Kalau belum ada, berhenti dan laporkan daftar elemen yang perlu ditambahkan dev FE. Jangan mengarang selector.

## Langkah

1. Baca `spec.md`, `suite.md`, dan hook suite yang sudah ada. Cek Page Object, Step, Action, dan Fixture yang bisa dipakai ulang sebelum membuat baru (`page-objects/`, `support/`, `fixtures/`).
2. **Tampilkan rencana dan tunggu persetujuan**: file yang akan dibuat atau diubah (Page Object, Step, hook, fixture, `web.test.ts`), selector baru yang dibutuhkan, dan data yang dibuat per spec.
3. Setelah disetujui, tulis dari bawah ke atas:
   1. Fixture `fixtures/<modul>.json` (data pre-setup, teks yang diassert). Tanpa password dan token, kredensial lewat `Spectra.env`.
   2. Page Object `page-objects/<NamaModul>Page/web.ts`: satu getter per elemen, nama sesuai fungsi elemen. Semua selector hanya di sini.
   3. Step di `support/steps/<camelCase>/` (`step.md` + `web.step.ts`) untuk alur yang dipakai lebih dari satu spec. Setelah Step dibuat, ubah baris langkah yang sesuai di spec.md menjadi `@step:<nama>` (spec dibuat tanpa `@step`), dan pastikan `Step.<nama>()` dipanggil di `web.test.ts`, kalau tidak lint gagal.
   4. Hook suite (`before`: login aktor sekali per suite dan seed data lewat API kalau perlu; `afterEach`/`after`: bersihkan data yang dibuat).
   5. `web.test.ts`: satu `it()`, judul sama dengan `title` di spec.md, satu assert atau aksi per langkah di spec.md, urutannya sama.
4. Data yang harus unik dibuat dengan suffix acak atau timestamp. Data tidak boleh diwariskan dari spec lain.
5. Setiap langkah `Verifikasi ...` di spec.md menjadi minimal satu assertion. Tidak boleh ada langkah spec yang tidak punya padanan di script.
6. Jalankan `spectra sync-types` kalau menambah Page Object, Step, atau Fixture, lalu `pnpm type-check` dan `spectra lint --strict <path>`.
7. Kalau lint dan type-check bersih, dan environment untuk menjalankan tersedia dan disetujui user, jalankan `spectra run "<path web.test.ts>" -t web`. Kalau berhasil, ubah `status` spec jadi `automated`. Kalau tidak bisa dijalankan, biarkan `ready-for-automation` dan laporkan alasannya.
8. Laporkan: file yang dibuat, hasil lint/type-check/run, dan selector atau data yang masih kurang.

## Aturan kode

- Zero import. Tidak ada `describe`, `test`, atau `it` kedua.
- Tanpa komentar di kode.
- Tanpa `Spectra.get(...)` atau selector mentah di `web.test.ts`. Semua lewat Page Object.
- Tidak ada teks UI atau data mentah yang diketik ulang di banyak tempat. Ambil dari fixture.
- Tanpa `sleep` atau jeda tetap. Pakai matcher dan `waitFor` yang tersedia di skill `matchers-and-assertions`.
- `Spectra.intercept()` hanya untuk error atau kondisi yang tidak bisa dipicu dengan aman (bagian 6 konvensi).
- Sebelum mengubah file yang sudah ada dan dipakai spec lain (Page Object, Step, fixture), cek pemakainya, dan minta izin kalau perubahan bisa memengaruhi spec lain.
